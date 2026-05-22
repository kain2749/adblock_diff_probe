# Adblock Diff Probe: rickroll_youtube

Target: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
Run directory: `runs/20260522_055723_utc`
Summary JSON: `runs/20260522_055723_utc/summary.json`

## Verdict

Possible anti-adblock behavior: **not proven from this run**

- No timing/text signal crossed the configured threshold.

Interpretation: compare playback timing separately from page-load timing. A large `time_to_playing` delta with a small `time_to_video_element` delta means the page produced a video element quickly, but playback was delayed.

## Median Comparison

| Metric | No blocker median | uBO median | Delta | Percent change |
|---|---:|---:|---:|---:|
| DOMContentLoaded | 1154 ms | n/a | n/a | n/a |
| Load event | 1181 ms | n/a | n/a | n/a |
| First contentful paint | 789 ms | n/a | n/a | n/a |
| Largest contentful paint | n/a | n/a | n/a | n/a |
| Time to video element | 18 ms | n/a | n/a | n/a |
| Time to playing | 121 ms | n/a | n/a | n/a |
| Video currentTime after wait | 11.14 s | n/a | n/a | n/a |
| Total run time | 17045 ms | n/a | n/a | n/a |

## Per-Run Timing

### no_blocker

| Run | DOMContentLoaded | Load | Video element | Playing | Video currentTime after wait | Anti-adblock text | Notes |
|---:|---:|---:|---:|---:|---:|---|---|
| 1 | 1154 ms | 1181 ms | 17 ms | 156 ms | 11.18 s | False |  |
| 2 | 1279 ms | 1383 ms | 18 ms | 121 ms | 11.14 s | False |  |
| 3 | 961 ms | 984 ms | 24 ms | 117 ms | 11.14 s | False |  |

## Per-Profile Timing Stats

### no_blocker

| Metric | Values | Min | Median | Mean | Max | Stdev |
|---|---|---:|---:|---:|---:|---:|
| DOMContentLoaded | `1279 ms, 1154 ms, 961 ms` | 961 ms | 1154 ms | 1131 ms | 1279 ms | 160 ms |
| Load event | `1383 ms, 1181 ms, 984 ms` | 984 ms | 1181 ms | 1183 ms | 1383 ms | 200 ms |
| First contentful paint | `789 ms, 1063 ms, 416 ms` | 416 ms | 789 ms | 756 ms | 1063 ms | 325 ms |
| Largest contentful paint | `n/a, n/a, n/a` | n/a | n/a | n/a | n/a | n/a |
| Time to video element | `18 ms, 17 ms, 24 ms` | 17 ms | 18 ms | 20 ms | 24 ms | 4 ms |
| Time to playing | `121 ms, 156 ms, 117 ms` | 117 ms | 121 ms | 131 ms | 156 ms | 21 ms |
| Video currentTime after wait | `11.14 s, 11.18 s, 11.14 s` | 11.14 s | 11.14 s | 11.15 s | 11.18 s | 0.02 s |
| Total run time | `17164 ms, 17045 ms, 16729 ms` | 16729 ms | 17045 ms | 16979 ms | 17164 ms | 225 ms |

## Detected Anti-Adblock Phrases

None detected in visible body text.

## Environment

| Field | Value |
|---|---|
| `python` | `3.10.12` |
| `platform` | `Linux-6.17.9-76061709-generic-x86_64-with-glibc2.35` |
| `system` | `Linux` |
| `machine` | `x86_64` |
| `firefox_version` | `Mozilla Firefox 151.0` |
| `selenium_version` | `4.44.0` |
| `target_url` | `https://www.youtube.com/watch?v=dQw4w9WgXcQ` |
| `viewport` | `1280x720` |
| `headless` | `False` |
| `runs_per_profile` | `3` |
| `navigation_timeout_s` | `45` |
| `video_timeout_s` | `20` |
| `settle_seconds` | `10` |
| `ubo_xpi_supplied` | `False` |

## Raw Outputs

Raw JSON and screenshots live under `runs/20260522_055723_utc`.
Machine-readable summary: `runs/20260522_055723_utc/summary.json`.

Careful wording for publication: this run shows a repeatable playback-start delay under this exact Firefox/Selenium/uBO setup. It does not prove every browser, account state, region, network, or uBO version gets the same delay.
