# Adblock Diff Probe: rickroll_youtube

Target: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
Run directory: `runs/20260522_055533_utc`
Summary JSON: `runs/20260522_055533_utc/summary.json`

## Verdict

Possible anti-adblock behavior: **not proven from this run**

- No timing/text signal crossed the configured threshold.

Interpretation: compare playback timing separately from page-load timing. A large `time_to_playing` delta with a small `time_to_video_element` delta means the page produced a video element quickly, but playback was delayed.

## Median Comparison

| Metric | No blocker median | uBO median | Delta | Percent change |
|---|---:|---:|---:|---:|
| DOMContentLoaded | 1229 ms | n/a | n/a | n/a |
| Load event | 1323 ms | n/a | n/a | n/a |
| First contentful paint | 898 ms | n/a | n/a | n/a |
| Largest contentful paint | n/a | n/a | n/a | n/a |
| Time to video element | 25 ms | n/a | n/a | n/a |
| Time to playing | 58 ms | n/a | n/a | n/a |
| Video currentTime after wait | 11.09 s | n/a | n/a | n/a |
| Total run time | 17137 ms | n/a | n/a | n/a |

## Per-Run Timing

### no_blocker

| Run | DOMContentLoaded | Load | Video element | Playing | Video currentTime after wait | Anti-adblock text | Notes |
|---:|---:|---:|---:|---:|---:|---|---|
| 1 | 1524 ms | 1548 ms | 24 ms | 18 ms | 11.51 s | False |  |
| 2 | 924 ms | 1027 ms | 28 ms | 60 ms | 11.09 s | False |  |
| 3 | 1229 ms | 1323 ms | 25 ms | 58 ms | 11.09 s | False |  |

## Per-Profile Timing Stats

### no_blocker

| Metric | Values | Min | Median | Mean | Max | Stdev |
|---|---|---:|---:|---:|---:|---:|
| DOMContentLoaded | `924 ms, 1229 ms, 1524 ms` | 924 ms | 1229 ms | 1226 ms | 1524 ms | 300 ms |
| Load event | `1027 ms, 1323 ms, 1548 ms` | 1027 ms | 1323 ms | 1299 ms | 1548 ms | 261 ms |
| First contentful paint | `538 ms, 898 ms, 931 ms` | 538 ms | 898 ms | 789 ms | 931 ms | 218 ms |
| Largest contentful paint | `n/a, n/a, n/a` | n/a | n/a | n/a | n/a | n/a |
| Time to video element | `28 ms, 25 ms, 24 ms` | 24 ms | 25 ms | 26 ms | 28 ms | 2 ms |
| Time to playing | `60 ms, 58 ms, 18 ms` | 18 ms | 58 ms | 45 ms | 60 ms | 24 ms |
| Video currentTime after wait | `11.09 s, 11.09 s, 11.51 s` | 11.09 s | 11.09 s | 11.23 s | 11.51 s | 0.24 s |
| Total run time | `16755 ms, 17246 ms, 17137 ms` | 16755 ms | 17137 ms | 17046 ms | 17246 ms | 258 ms |

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

Raw JSON and screenshots live under `runs/20260522_055533_utc`.
Machine-readable summary: `runs/20260522_055533_utc/summary.json`.

Careful wording for publication: this run shows a repeatable playback-start delay under this exact Firefox/Selenium/uBO setup. It does not prove every browser, account state, region, network, or uBO version gets the same delay.
