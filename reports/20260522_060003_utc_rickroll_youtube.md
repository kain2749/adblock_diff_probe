# Adblock Diff Probe: rickroll_youtube

Target: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
Run directory: `runs/20260522_060003_utc`
Summary JSON: `runs/20260522_060003_utc/summary.json`

## Verdict

Possible anti-adblock behavior: **YES**

- uBO median time-to-playing was 7508 ms slower

Interpretation: compare playback timing separately from page-load timing. A large `time_to_playing` delta with a small `time_to_video_element` delta means the page produced a video element quickly, but playback was delayed.

## Median Comparison

| Metric | No blocker median | uBO median | Delta | Percent change |
|---|---:|---:|---:|---:|
| DOMContentLoaded | 1214 ms | 1672 ms | 457 ms | +37.6% |
| Load event | 1238 ms | 1750 ms | 512 ms | +41.4% |
| First contentful paint | 738 ms | 1100 ms | 362 ms | +49.1% |
| Largest contentful paint | n/a | n/a | n/a | n/a |
| Time to video element | 18 ms | 18 ms | -0 ms | -2.8% |
| Time to playing | 156 ms | 7664 ms | 7508 ms | +4797.4% |
| Video currentTime after wait | 11.18 s | 11.05 s | -0.13 s | -1.2% |
| Total run time | 17072 ms | 27046 ms | 9973 ms | +58.4% |

## Per-Run Timing

### no_blocker

| Run | DOMContentLoaded | Load | Video element | Playing | Video currentTime after wait | Anti-adblock text | Notes |
|---:|---:|---:|---:|---:|---:|---|---|
| 1 | 1275 ms | 1371 ms | 20 ms | 128 ms | 11.14 s | False |  |
| 2 | 1521 ms | 1544 ms | 13 ms | 167 ms | 11.18 s | False |  |
| 3 | 1198 ms | 1222 ms | 23 ms | 158 ms | 11.19 s | False |  |
| 4 | 1393 ms | 1497 ms | 19 ms | 155 ms | 11.18 s | False |  |
| 5 | 885 ms | 995 ms | 13 ms | 60 ms | 11.09 s | False |  |
| 6 | 1231 ms | 1254 ms | 11 ms | 609 ms | 11.64 s | False |  |
| 7 | 1519 ms | 1542 ms | 12 ms | 31 ms | 11.64 s | False |  |
| 8 | 1035 ms | 1081 ms | 53 ms | 36 ms | 11.09 s | False |  |
| 9 | 974 ms | 1075 ms | 17 ms | 158 ms | 11.18 s | False |  |
| 10 | 995 ms | 1099 ms | 36 ms | 166 ms | 11.18 s | False |  |

### ubo

| Run | DOMContentLoaded | Load | Video element | Playing | Video currentTime after wait | Anti-adblock text | Notes |
|---:|---:|---:|---:|---:|---:|---|---|
| 1 | 1662 ms | 1797 ms | 2 ms | 3660 ms | 11.11 s | False | installed addon: uBlock0@raymondhill.net |
| 2 | 1863 ms | 1886 ms | 12 ms | 3683 ms | 11.10 s | False | installed addon: uBlock0@raymondhill.net |
| 3 | 1978 ms | 2004 ms | 27 ms | 3162 ms | 11.04 s | False | installed addon: uBlock0@raymondhill.net |
| 4 | 1474 ms | 1511 ms | 9 ms | 243 ms | 11.00 s | False | installed addon: uBlock0@raymondhill.net |
| 5 | 1681 ms | 1704 ms | 25 ms | 11758 ms | 11.03 s | False | installed addon: uBlock0@raymondhill.net |
| 6 | 1441 ms | 1477 ms | 13 ms | 11971 ms | 11.05 s | False | installed addon: uBlock0@raymondhill.net |
| 7 | 1322 ms | 1345 ms | 17 ms | 3682 ms | 11.12 s | False | installed addon: uBlock0@raymondhill.net |
| 8 | 1779 ms | 1802 ms | 31 ms | 11648 ms | 11.04 s | False | installed addon: uBlock0@raymondhill.net |
| 9 | 1313 ms | 1334 ms | 41 ms | 11646 ms | 11.03 s | False | installed addon: uBlock0@raymondhill.net |
| 10 | 1783 ms | 1803 ms | 18 ms | 11701 ms | 11.06 s | False | installed addon: uBlock0@raymondhill.net |

## Per-Profile Timing Stats

### no_blocker

| Metric | Values | Min | Median | Mean | Max | Stdev |
|---|---|---:|---:|---:|---:|---:|
| DOMContentLoaded | `995 ms, 885 ms, 1275 ms, 1231 ms, 1521 ms, 1519 ms, 1393 ms, 1035 ms, 1198 ms, 974 ms` | 885 ms | 1214 ms | 1203 ms | 1521 ms | 228 ms |
| Load event | `1099 ms, 995 ms, 1371 ms, 1254 ms, 1544 ms, 1542 ms, 1497 ms, 1081 ms, 1222 ms, 1075 ms` | 995 ms | 1238 ms | 1268 ms | 1544 ms | 209 ms |
| First contentful paint | `627 ms, 496 ms, 819 ms, 1143 ms, 1425 ms, 912 ms, 1377 ms, 460 ms, 657 ms, 584 ms` | 460 ms | 738 ms | 850 ms | 1425 ms | 355 ms |
| Largest contentful paint | `n/a, n/a, n/a, n/a, n/a, n/a, n/a, n/a, n/a, n/a` | n/a | n/a | n/a | n/a | n/a |
| Time to video element | `36 ms, 13 ms, 20 ms, 11 ms, 13 ms, 12 ms, 19 ms, 53 ms, 23 ms, 17 ms` | 11 ms | 18 ms | 22 ms | 53 ms | 13 ms |
| Time to playing | `166 ms, 60 ms, 128 ms, 609 ms, 167 ms, 31 ms, 155 ms, 36 ms, 158 ms, 158 ms` | 31 ms | 156 ms | 167 ms | 609 ms | 165 ms |
| Video currentTime after wait | `11.18 s, 11.09 s, 11.14 s, 11.64 s, 11.18 s, 11.64 s, 11.18 s, 11.09 s, 11.19 s, 11.18 s` | 11.09 s | 11.18 s | 11.25 s | 11.64 s | 0.21 s |
| Total run time | `16884 ms, 16704 ms, 17227 ms, 17472 ms, 17311 ms, 17348 ms, 17418 ms, 16864 ms, 16918 ms, 16791 ms` | 16704 ms | 17072 ms | 17094 ms | 17472 ms | 288 ms |

### ubo

| Metric | Values | Min | Median | Mean | Max | Stdev |
|---|---|---:|---:|---:|---:|---:|
| DOMContentLoaded | `1662 ms, 1681 ms, 1313 ms, 1863 ms, 1783 ms, 1474 ms, 1322 ms, 1441 ms, 1978 ms, 1779 ms` | 1313 ms | 1672 ms | 1630 ms | 1978 ms | 231 ms |
| Load event | `1797 ms, 1704 ms, 1334 ms, 1886 ms, 1803 ms, 1511 ms, 1345 ms, 1477 ms, 2004 ms, 1802 ms` | 1334 ms | 1750 ms | 1666 ms | 2004 ms | 234 ms |
| First contentful paint | `1156 ms, 1042 ms, 695 ms, 1285 ms, 1177 ms, 1470 ms, 709 ms, 878 ms, 1044 ms, 1173 ms` | 695 ms | 1100 ms | 1063 ms | 1470 ms | 246 ms |
| Largest contentful paint | `n/a, n/a, n/a, n/a, n/a, n/a, n/a, n/a, n/a, n/a` | n/a | n/a | n/a | n/a | n/a |
| Time to video element | `2 ms, 25 ms, 41 ms, 12 ms, 18 ms, 9 ms, 17 ms, 13 ms, 27 ms, 31 ms` | 2 ms | 18 ms | 20 ms | 41 ms | 12 ms |
| Time to playing | `3660 ms, 11758 ms, 11646 ms, 3683 ms, 11701 ms, 243 ms, 3682 ms, 11971 ms, 3162 ms, 11648 ms` | 243 ms | 7664 ms | 7315 ms | 11971 ms | 4775 ms |
| Video currentTime after wait | `11.11 s, 11.03 s, 11.03 s, 11.10 s, 11.06 s, 11.00 s, 11.12 s, 11.05 s, 11.04 s, 11.04 s` | 11.00 s | 11.05 s | 11.06 s | 11.12 s | 0.04 s |
| Total run time | `22881 ms, 31616 ms, 30520 ms, 23571 ms, 31589 ms, 19418 ms, 22551 ms, 31714 ms, 22904 ms, 30882 ms` | 19418 ms | 27046 ms | 26765 ms | 31714 ms | 4879 ms |

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
| `runs_per_profile` | `10` |
| `navigation_timeout_s` | `45` |
| `video_timeout_s` | `20` |
| `settle_seconds` | `10` |
| `ubo_xpi_supplied` | `True` |

## Raw Outputs

Raw JSON and screenshots live under `runs/20260522_060003_utc`.
Machine-readable summary: `runs/20260522_060003_utc/summary.json`.

Careful wording for publication: this run shows a repeatable playback-start delay under this exact Firefox/Selenium/uBO setup. It does not prove every browser, account state, region, network, or uBO version gets the same delay.
