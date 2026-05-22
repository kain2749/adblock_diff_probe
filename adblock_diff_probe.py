#!/usr/bin/env python
"""
adblock_diff_probe_firefox.py

MVP web behavior diff harness using Selenium + Firefox.
Hardcoded first target: YouTube Rickroll.

Runs the same URL in two Firefox profiles:
  1. no_blocker
  2. ubo, if --ubo-xpi is supplied

Outputs:
  runs/<timestamp>/<profile>/run_<n>.json
  runs/<timestamp>/<profile>/run_<n>.png
  reports/<timestamp>_rickroll_youtube.md

This measures behavior. It does not bypass anything.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
import shutil
import statistics
import time
from collections import defaultdict
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait

TARGET_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
TARGET_NAME = "rickroll_youtube"
VIEWPORT_WIDTH = 1280
VIEWPORT_HEIGHT = 720

ANTI_ADBLOCK_PATTERNS = [
    r"ad blocker",
    r"adblock",
    r"disable your ad",
    r"disable ad",
    r"turn off your ad",
    r"allow ads",
    r"whitelist",
    r"white list",
    r"support us by allowing ads",
    r"ads help",
    r"blocked by client",
]

@dataclass
class ProbeResult:
    url: str
    profile: str
    run_index: int
    started_at_utc: str
    user_agent: str | None
    domcontentloaded_ms: int | None
    load_ms: int | None
    first_contentful_paint_ms: float | None
    largest_contentful_paint_ms: float | None
    time_to_video_element_ms: int | None
    time_to_playing_ms: int | None
    video_current_time_after_wait_s: float | None
    video_paused_after_wait: bool | None
    video_ready_state_after_wait: int | None
    video_error_after_wait: str | None
    anti_adblock_text_detected: bool
    detected_phrases: list[str]
    visible_text_length: int | None
    visible_text_hash: str | None
    screenshot_path: str
    total_run_ms: int
    notes: list[str]


def now_slug() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S_utc")


def mkdir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", errors="replace")).hexdigest()


def median_or_none(values: list[float | int | None]) -> float | None:
    good = [v for v in values if v is not None]
    if not good:
        return None
    return float(statistics.median(good))


def fmt_ms(v: float | int | None) -> str:
    if v is None:
        return "n/a"
    return f"{v:.0f} ms"


def fmt_num(v: float | int | None) -> str:
    if v is None:
        return "n/a"
    if isinstance(v, float):
        return f"{v:.2f}"
    return str(v)


def get_perf_metrics(driver: webdriver.Firefox) -> dict[str, float | None]:
    try:
        return driver.execute_script(
            """
            const nav = performance.getEntriesByType('navigation')[0];
            const paints = performance.getEntriesByType('paint');
            const fcp = paints.find(p => p.name === 'first-contentful-paint');
            const lcps = performance.getEntriesByType('largest-contentful-paint');
            const lcp = lcps.length ? lcps[lcps.length - 1].startTime : null;
            return {
              domcontentloaded_ms: nav ? nav.domContentLoadedEventEnd : null,
              load_ms: nav ? nav.loadEventEnd : null,
              first_contentful_paint_ms: fcp ? fcp.startTime : null,
              largest_contentful_paint_ms: lcp,
            };
            """
        )
    except Exception:
        return {
            "domcontentloaded_ms": None,
            "load_ms": None,
            "first_contentful_paint_ms": None,
            "largest_contentful_paint_ms": None,
        }


def visible_text_info(driver: webdriver.Firefox) -> tuple[int | None, str | None, bool, list[str]]:
    try:
        text = driver.find_element("tag name", "body").text
    except Exception:
        return None, None, False, []

    text_lower = text.lower()
    detected: list[str] = []
    for pat in ANTI_ADBLOCK_PATTERNS:
        if re.search(pat, text_lower, re.IGNORECASE):
            detected.append(pat)

    return len(text), sha256_text(text), bool(detected), detected[:20]


def force_video_play(driver: webdriver.Firefox) -> None:
    try:
        driver.execute_script(
            """
            const v = document.querySelector('video');
            if (v) {
              v.muted = true;
              v.play().catch(() => {});
            }
            """
        )
    except Exception:
        pass


def wait_for_video_element(driver: webdriver.Firefox, timeout_s: float) -> tuple[int | None, list[str]]:
    start = time.monotonic()
    notes: list[str] = []
    try:
        WebDriverWait(driver, timeout_s).until(
            lambda d: d.execute_script("return !!document.querySelector('video');")
        )
        return int((time.monotonic() - start) * 1000), notes
    except TimeoutException:
        notes.append(f"video element not found within {timeout_s:.1f}s")
        return None, notes


def wait_for_playing(driver: webdriver.Firefox, timeout_s: float) -> tuple[int | None, list[str]]:
    start = time.monotonic()
    notes: list[str] = []
    force_video_play(driver)
    try:
        WebDriverWait(driver, timeout_s, poll_frequency=0.1).until(
            lambda d: d.execute_script(
                """
                const v = document.querySelector('video');
                return !!(v && !v.paused && v.readyState >= 2 && v.currentTime > 0);
                """
            )
        )
        return int((time.monotonic() - start) * 1000), notes
    except TimeoutException:
        notes.append(f"video did not enter playing/currentTime>0 within {timeout_s:.1f}s")
        return None, notes


def video_state(driver: webdriver.Firefox) -> dict[str, Any]:
    try:
        return driver.execute_script(
            """
            const v = document.querySelector('video');
            if (!v) {
              return {found: false, currentTime: null, paused: null, readyState: null, error: null};
            }
            return {
              found: true,
              currentTime: v.currentTime,
              paused: v.paused,
              readyState: v.readyState,
              error: v.error ? String(v.error.code) : null
            };
            """
        )
    except Exception as exc:
        return {"found": False, "currentTime": None, "paused": None, "readyState": None, "error": type(exc).__name__}


def make_firefox_driver(profile_dir: Path, headless: bool, page_load_timeout_s: int) -> webdriver.Firefox:
    opts = Options()
    if headless:
        opts.add_argument("-headless")

    opts.set_preference("media.autoplay.default", 0)
    opts.set_preference("media.autoplay.blocking_policy", 0)
    opts.set_preference("media.volume_scale", "0.0")
    opts.set_preference("dom.webnotifications.enabled", False)
    opts.set_preference("privacy.trackingprotection.enabled", False)
    opts.set_preference("browser.shell.checkDefaultBrowser", False)
    opts.set_preference("browser.startup.homepage_override.mstone", "ignore")
    opts.set_preference("startup.homepage_welcome_url", "about:blank")
    opts.set_preference("startup.homepage_welcome_url.additional", "about:blank")
    opts.profile = str(profile_dir)

    driver = webdriver.Firefox(options=opts, service=Service())
    driver.set_page_load_timeout(page_load_timeout_s)
    driver.set_window_size(VIEWPORT_WIDTH, VIEWPORT_HEIGHT)
    return driver


def run_probe(
    profile: str,
    run_index: int,
    run_dir: Path,
    ubo_xpi: Path | None,
    navigation_timeout_s: int,
    video_timeout_s: int,
    settle_seconds: int,
    headless: bool,
) -> ProbeResult:
    profile_dir = mkdir(run_dir / "profiles" / f"{profile}_{run_index}")
    output_dir = mkdir(run_dir / profile)
    screenshot_path = output_dir / f"run_{run_index}.png"

    started_wall = datetime.now(timezone.utc).isoformat()
    run_start = time.monotonic()
    notes: list[str] = []

    driver = make_firefox_driver(profile_dir, headless=headless, page_load_timeout_s=navigation_timeout_s)

    try:
        if ubo_xpi is not None:
            try:
                addon_id = driver.install_addon(str(ubo_xpi), temporary=True)
                notes.append(f"installed addon: {addon_id}")
                # Give uBO a moment to initialize. Without this, first navigation can race the extension startup.
                time.sleep(2)
            except Exception as exc:
                notes.append(f"uBO install failed: {type(exc).__name__}: {exc}")

        user_agent = None
        try:
            user_agent = driver.execute_script("return navigator.userAgent;")
        except Exception:
            pass

        try:
            driver.get(TARGET_URL)
        except TimeoutException:
            notes.append("driver.get timed out; continuing with whatever loaded")
        except WebDriverException as exc:
            notes.append(f"driver.get WebDriverException: {exc}")

        perf = get_perf_metrics(driver)

        time_to_video_element_ms, video_notes = wait_for_video_element(driver, timeout_s=video_timeout_s)
        notes.extend(video_notes)

        time_to_playing_ms, playing_notes = wait_for_playing(driver, timeout_s=video_timeout_s)
        notes.extend(playing_notes)

        time.sleep(settle_seconds)
        force_video_play(driver)
        time.sleep(1)

        vstate = video_state(driver)
        visible_len, visible_hash, anti_detected, detected_phrases = visible_text_info(driver)

        try:
            driver.save_screenshot(str(screenshot_path))
        except Exception as exc:
            notes.append(f"screenshot failed: {type(exc).__name__}: {exc}")

        result = ProbeResult(
            url=TARGET_URL,
            profile=profile,
            run_index=run_index,
            started_at_utc=started_wall,
            user_agent=user_agent,
            domcontentloaded_ms=int(perf["domcontentloaded_ms"]) if perf.get("domcontentloaded_ms") is not None else None,
            load_ms=int(perf["load_ms"]) if perf.get("load_ms") is not None else None,
            first_contentful_paint_ms=perf.get("first_contentful_paint_ms"),
            largest_contentful_paint_ms=perf.get("largest_contentful_paint_ms"),
            time_to_video_element_ms=time_to_video_element_ms,
            time_to_playing_ms=time_to_playing_ms,
            video_current_time_after_wait_s=vstate.get("currentTime"),
            video_paused_after_wait=vstate.get("paused"),
            video_ready_state_after_wait=vstate.get("readyState"),
            video_error_after_wait=vstate.get("error"),
            anti_adblock_text_detected=anti_detected,
            detected_phrases=detected_phrases,
            visible_text_length=visible_len,
            visible_text_hash=visible_hash,
            screenshot_path=str(screenshot_path),
            total_run_ms=int((time.monotonic() - run_start) * 1000),
            notes=notes,
        )

        json_path = output_dir / f"run_{run_index}.json"
        json_path.write_text(json.dumps(asdict(result), indent=2, sort_keys=True), encoding="utf-8")
        return result

    finally:
        try:
            driver.quit()
        except Exception:
            pass


def summarize_profile(results: list[ProbeResult]) -> dict[str, Any]:
    return {
        "runs": len(results),
        "median_domcontentloaded_ms": median_or_none([r.domcontentloaded_ms for r in results]),
        "median_load_ms": median_or_none([r.load_ms for r in results]),
        "median_fcp_ms": median_or_none([r.first_contentful_paint_ms for r in results]),
        "median_lcp_ms": median_or_none([r.largest_contentful_paint_ms for r in results]),
        "median_time_to_video_element_ms": median_or_none([r.time_to_video_element_ms for r in results]),
        "median_time_to_playing_ms": median_or_none([r.time_to_playing_ms for r in results]),
        "median_video_current_time_after_wait_s": median_or_none([r.video_current_time_after_wait_s for r in results]),
        "anti_adblock_text_detected_any": any(r.anti_adblock_text_detected for r in results),
        "detected_phrases": sorted(set().union(*(set(r.detected_phrases) for r in results))) if results else [],
    }


def delta(new: float | None, old: float | None) -> float | None:
    if new is None or old is None:
        return None
    return new - old


def write_report(run_dir: Path, report_path: Path, results_by_profile: dict[str, list[ProbeResult]]) -> None:
    no_blocker = summarize_profile(results_by_profile.get("no_blocker", []))
    ubo = summarize_profile(results_by_profile.get("ubo", []))

    playing_delta = delta(ubo.get("median_time_to_playing_ms"), no_blocker.get("median_time_to_playing_ms"))

    possible_anti = False
    reasons: list[str] = []
    if playing_delta is not None and playing_delta > 1500:
        possible_anti = True
        reasons.append(f"uBO median time-to-playing was {playing_delta:.0f} ms slower")
    if ubo.get("anti_adblock_text_detected_any"):
        possible_anti = True
        reasons.append("visible anti-adblock text detected")

    lines: list[str] = []
    lines.append(f"# Adblock Diff Probe: {TARGET_NAME}")
    lines.append("")
    lines.append(f"Target: `{TARGET_URL}`")
    lines.append(f"Run directory: `{run_dir}`")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"Possible anti-adblock behavior: **{'YES' if possible_anti else 'not proven from this run'}**")
    if reasons:
        lines.append("")
        for reason in reasons:
            lines.append(f"- {reason}")
    lines.append("")
    lines.append("## Median Metrics")
    lines.append("")
    lines.append("| Metric | No blocker | uBO | Delta |")
    lines.append("|---|---:|---:|---:|")
    metric_rows = [
        ("DOMContentLoaded", "median_domcontentloaded_ms", "ms"),
        ("Load event", "median_load_ms", "ms"),
        ("First contentful paint", "median_fcp_ms", "ms"),
        ("Largest contentful paint", "median_lcp_ms", "ms"),
        ("Time to video element", "median_time_to_video_element_ms", "ms"),
        ("Time to playing", "median_time_to_playing_ms", "ms"),
        ("Video currentTime after wait", "median_video_current_time_after_wait_s", "s"),
    ]
    for label, key, unit in metric_rows:
        a = no_blocker.get(key)
        b = ubo.get(key)
        d = delta(b, a)
        if unit == "ms":
            lines.append(f"| {label} | {fmt_ms(a)} | {fmt_ms(b)} | {fmt_ms(d)} |")
        else:
            lines.append(f"| {label} | {fmt_num(a)} | {fmt_num(b)} | {fmt_num(d)} |")

    lines.append("")
    lines.append("## Detected Anti-Adblock Phrases")
    lines.append("")
    phrases = ubo.get("detected_phrases", [])
    if phrases:
        for p in phrases:
            lines.append(f"- `{p}`")
    else:
        lines.append("None detected in visible body text.")

    lines.append("")
    lines.append("## Per-Run Details")
    lines.append("")
    for profile, results in results_by_profile.items():
        lines.append(f"### {profile}")
        lines.append("")
        lines.append("| Run | Time to playing | Video currentTime after wait | Anti-adblock text | Notes |")
        lines.append("|---:|---:|---:|---|---|")
        for r in sorted(results, key=lambda x: x.run_index):
            notes = "; ".join(r.notes).replace("|", "\\|") if r.notes else ""
            lines.append(
                f"| {r.run_index} | {fmt_ms(r.time_to_playing_ms)} | "
                f"{fmt_num(r.video_current_time_after_wait_s)} | "
                f"{r.anti_adblock_text_detected} | {notes} |"
            )
        lines.append("")

    lines.append("## Raw Outputs")
    lines.append("")
    lines.append(f"JSON and screenshots live under `{run_dir}`.")

    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Measure webpage behavior with and without uBO using Firefox/Selenium.")
    parser.add_argument("--runs", type=int, default=3, help="Runs per profile. Default: 3")
    parser.add_argument("--ubo-xpi", type=Path, default=None, help="Path to uBlock Origin Firefox .xpi")
    parser.add_argument("--out", type=Path, default=Path("."), help="Output root. Default: current directory")
    parser.add_argument("--navigation-timeout-s", type=int, default=45)
    parser.add_argument("--video-timeout-s", type=int, default=20)
    parser.add_argument("--settle-seconds", type=int, default=10, help="Seconds to wait after playback attempt before sampling video state.")
    parser.add_argument("--headless", action="store_true", help="Run headless. Use headful first while testing.")
    parser.add_argument("--keep-profiles", action="store_true", help="Keep generated Firefox profile directories.")
    args = parser.parse_args()

    if args.runs < 1:
        raise SystemExit("--runs must be >= 1")

    if args.ubo_xpi is not None and not args.ubo_xpi.exists():
        raise SystemExit(f"uBO XPI does not exist: {args.ubo_xpi}")

    ts = now_slug()
    run_dir = mkdir(args.out / "runs" / ts)
    report_dir = mkdir(args.out / "reports")
    report_path = report_dir / f"{ts}_{TARGET_NAME}.md"

    plan: list[tuple[str, Path | None, int]] = []
    for i in range(1, args.runs + 1):
        plan.append(("no_blocker", None, i))
        if args.ubo_xpi is not None:
            plan.append(("ubo", args.ubo_xpi.resolve(), i))

    random.shuffle(plan)

    results_by_profile: dict[str, list[ProbeResult]] = defaultdict(list)

    for profile, xpi, run_index in plan:
        print(f"[*] Running {profile} #{run_index} ...")
        result = run_probe(
            profile=profile,
            run_index=run_index,
            run_dir=run_dir,
            ubo_xpi=xpi,
            navigation_timeout_s=args.navigation_timeout_s,
            video_timeout_s=args.video_timeout_s,
            settle_seconds=args.settle_seconds,
            headless=args.headless,
        )
        results_by_profile[profile].append(result)
        print(
            f"    playing={fmt_ms(result.time_to_playing_ms)} "
            f"video_t={fmt_num(result.video_current_time_after_wait_s)}s "
            f"anti_text={result.anti_adblock_text_detected}"
        )

    write_report(run_dir=run_dir, report_path=report_path, results_by_profile=results_by_profile)

    if not args.keep_profiles:
        profiles_dir = run_dir / "profiles"
        if profiles_dir.exists():
            shutil.rmtree(profiles_dir)

    print(f"\n[+] Report: {report_path}")
    print(f"[+] Raw run data: {run_dir}")


if __name__ == "__main__":
    main()

