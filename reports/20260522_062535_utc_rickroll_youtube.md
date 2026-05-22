# Adblock Diff Probe: rickroll_youtube

Target: `https://www.youtube.com/watch?v=Bu_N_Bk7nDY`
Run directory: `runs/20260522_062535_utc`
Summary JSON: `runs/20260522_062535_utc/summary.json`

## Verdict

Possible anti-adblock behavior: **not proven from this run**

- No timing/text signal crossed the configured threshold.

Interpretation: compare playback timing separately from page-load timing. A large `time_to_playing` delta with a small `time_to_video_element` delta means the page produced a video element quickly, but playback was delayed.

## Median Comparison

| Metric | No blocker median | uBO median | Delta | Percent change |
|---|---:|---:|---:|---:|
| DOMContentLoaded | 1960 ms | 2033 ms | 73 ms | +3.7% |
| Load event | 1984 ms | 2071 ms | 86 ms | +4.4% |
| First contentful paint | 1004 ms | 1160 ms | 157 ms | +15.6% |
| Largest contentful paint | n/a | n/a | n/a | n/a |
| Time to video element | 38 ms | 32 ms | -6 ms | -16.0% |
| Time to playing | 38 ms | 33 ms | -6 ms | -14.3% |
| Video currentTime after wait | 11.86 s | 11.83 s | -0.02 s | -0.2% |
| Total run time | 18590 ms | 21301 ms | 2712 ms | +14.6% |

## Per-Run Timing

### no_blocker

| Run | DOMContentLoaded | Load | Video element | Playing | Video currentTime after wait | Anti-adblock text | Notes |
|---:|---:|---:|---:|---:|---:|---|---|
| 1 | 1776 ms | 1800 ms | 39 ms | 17 ms | 11.72 s | False |  |
| 2 | 1220 ms | 1257 ms | 135 ms | 30 ms | 11.17 s | False |  |
| 3 | 1442 ms | 1479 ms | 49 ms | 152 ms | 11.20 s | False |  |
| 4 | 2612 ms | 2666 ms | 5 ms | 45 ms | 12.14 s | False |  |
| 5 | 4880 ms | 4936 ms | 22 ms | 56 ms | 13.22 s | False |  |
| 6 | 1316 ms | 1357 ms | 157 ms | 55 ms | 11.24 s | False |  |
| 7 | 2144 ms | 2169 ms | 36 ms | 26 ms | 11.88 s | False |  |
| 8 | 3203 ms | 3552 ms | 9 ms | 38 ms | 13.04 s | False |  |
| 9 | 2427 ms | 2446 ms | 43 ms | 39 ms | 12.43 s | False |  |
| 10 | 1564 ms | 1588 ms | 34 ms | 36 ms | 11.83 s | False |  |

### ubo

| Run | DOMContentLoaded | Load | Video element | Playing | Video currentTime after wait | Anti-adblock text | Notes |
|---:|---:|---:|---:|---:|---:|---|---|
| 1 | 2319 ms | 2347 ms | 30 ms | 35 ms | 11.87 s | False | installed addon: uBlock0@raymondhill.net |
| 2 | 2390 ms | 2419 ms | 34 ms | 22 ms | 12.13 s | False | installed addon: uBlock0@raymondhill.net |
| 3 | 1463 ms | 1517 ms | 4 ms | 50 ms | 11.65 s | False | installed addon: uBlock0@raymondhill.net |
| 4 | 1599 ms | 1626 ms | 31 ms | 27 ms | 11.80 s | False | installed addon: uBlock0@raymondhill.net |
| 5 | 1598 ms | 1626 ms | 52 ms | 64 ms | 11.78 s | False | installed addon: uBlock0@raymondhill.net |
| 6 | 2595 ms | 2627 ms | 46 ms | 29 ms | 11.97 s | False | installed addon: uBlock0@raymondhill.net |
| 7 | 2433 ms | 2468 ms | 82 ms | 44 ms | 12.20 s | False | installed addon: uBlock0@raymondhill.net |
| 8 | 2393 ms | 2440 ms | 23 ms | 53 ms | 12.34 s | False | installed addon: uBlock0@raymondhill.net |
| 9 | 1747 ms | 1795 ms | 20 ms | 31 ms | 11.69 s | False | installed addon: uBlock0@raymondhill.net |
| 10 | 1686 ms | 1713 ms | 32 ms | 21 ms | 11.79 s | False | installed addon: uBlock0@raymondhill.net |

## Per-Profile Timing Stats

### no_blocker

| Metric | Values | Min | Median | Mean | Max | Stdev |
|---|---|---:|---:|---:|---:|---:|
| DOMContentLoaded | `3203 ms, 2612 ms, 1442 ms, 2427 ms, 4880 ms, 2144 ms, 1316 ms, 1220 ms, 1564 ms, 1776 ms` | 1220 ms | 1960 ms | 2258 ms | 4880 ms | 1119 ms |
| Load event | `3552 ms, 2666 ms, 1479 ms, 2446 ms, 4936 ms, 2169 ms, 1357 ms, 1257 ms, 1588 ms, 1800 ms` | 1257 ms | 1984 ms | 2325 ms | 4936 ms | 1159 ms |
| First contentful paint | `1377 ms, 1404 ms, 819 ms, 954 ms, 2657 ms, 1300 ms, 851 ms, 707 ms, 780 ms, 1053 ms` | 707 ms | 1004 ms | 1190 ms | 2657 ms | 575 ms |
| Largest contentful paint | `n/a, n/a, n/a, n/a, n/a, n/a, n/a, n/a, n/a, n/a` | n/a | n/a | n/a | n/a | n/a |
| Time to video element | `9 ms, 5 ms, 49 ms, 43 ms, 22 ms, 36 ms, 157 ms, 135 ms, 34 ms, 39 ms` | 5 ms | 38 ms | 53 ms | 157 ms | 51 ms |
| Time to playing | `38 ms, 45 ms, 152 ms, 39 ms, 56 ms, 26 ms, 55 ms, 30 ms, 36 ms, 17 ms` | 17 ms | 38 ms | 49 ms | 152 ms | 38 ms |
| Video currentTime after wait | `13.04 s, 12.14 s, 11.20 s, 12.43 s, 13.22 s, 11.88 s, 11.24 s, 11.17 s, 11.83 s, 11.72 s` | 11.17 s | 11.86 s | 11.99 s | 13.22 s | 0.73 s |
| Total run time | `20042 ms, 20525 ms, 17913 ms, 19652 ms, 21484 ms, 19033 ms, 18146 ms, 17265 ms, 17501 ms, 18131 ms` | 17265 ms | 18590 ms | 18969 ms | 21484 ms | 1411 ms |

### ubo

| Metric | Values | Min | Median | Mean | Max | Stdev |
|---|---|---:|---:|---:|---:|---:|
| DOMContentLoaded | `2433 ms, 1747 ms, 1463 ms, 1599 ms, 2595 ms, 2390 ms, 2393 ms, 2319 ms, 1686 ms, 1598 ms` | 1463 ms | 2033 ms | 2022 ms | 2595 ms | 437 ms |
| Load event | `2468 ms, 1795 ms, 1517 ms, 1626 ms, 2627 ms, 2419 ms, 2440 ms, 2347 ms, 1713 ms, 1626 ms` | 1517 ms | 2071 ms | 2058 ms | 2627 ms | 435 ms |
| First contentful paint | `1359 ms, 1075 ms, 889 ms, 868 ms, 1705 ms, 1247 ms, 1246 ms, 1466 ms, 928 ms, 847 ms` | 847 ms | 1160 ms | 1163 ms | 1705 ms | 291 ms |
| Largest contentful paint | `n/a, n/a, n/a, n/a, n/a, n/a, n/a, n/a, n/a, n/a` | n/a | n/a | n/a | n/a | n/a |
| Time to video element | `82 ms, 20 ms, 4 ms, 31 ms, 46 ms, 34 ms, 23 ms, 30 ms, 32 ms, 52 ms` | 4 ms | 32 ms | 35 ms | 82 ms | 21 ms |
| Time to playing | `44 ms, 31 ms, 50 ms, 27 ms, 29 ms, 22 ms, 53 ms, 35 ms, 21 ms, 64 ms` | 21 ms | 33 ms | 38 ms | 64 ms | 14 ms |
| Video currentTime after wait | `12.20 s, 11.69 s, 11.65 s, 11.80 s, 11.97 s, 12.13 s, 12.34 s, 11.87 s, 11.79 s, 11.78 s` | 11.65 s | 11.83 s | 11.92 s | 12.34 s | 0.23 s |
| Total run time | `21324 ms, 23935 ms, 20497 ms, 19650 ms, 21278 ms, 21755 ms, 20687 ms, 21661 ms, 21416 ms, 20496 ms` | 19650 ms | 21301 ms | 21270 ms | 23935 ms | 1139 ms |

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
| `target_url` | `https://www.youtube.com/watch?v=Bu_N_Bk7nDY` |
| `viewport` | `1280x720` |
| `headless` | `False` |
| `runs_per_profile` | `10` |
| `navigation_timeout_s` | `45` |
| `video_timeout_s` | `20` |
| `settle_seconds` | `10` |
| `ubo_xpi_supplied` | `True` |

## Raw Outputs

Raw JSON and screenshots live under `runs/20260522_062535_utc`.
Machine-readable summary: `runs/20260522_062535_utc/summary.json`.

Careful wording for publication: this run shows a repeatable playback-start delay under this exact Firefox/Selenium/uBO setup. It does not prove every browser, account state, region, network, or uBO version gets the same delay.
