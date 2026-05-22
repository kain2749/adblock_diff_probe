# Adblock Diff Probe: rickroll_youtube

Target: `https://www.youtube.com/watch?v=Bu_N_Bk7nDY`
Run directory: `runs/20260522_172015_utc`
Summary JSON: `runs/20260522_172015_utc/summary.json`

## Verdict

Possible anti-adblock behavior: **not proven from this run**

- No timing/text signal crossed the configured threshold.

Interpretation: compare playback timing separately from page-load timing. A large `time_to_playing` delta with a small `time_to_video_element` delta means the page produced a video element quickly, but playback was delayed.

## Median Comparison

| Metric | No blocker median | uBO median | Delta | Percent change |
|---|---:|---:|---:|---:|
| DOMContentLoaded | 1189 ms | 1695 ms | 506 ms | +42.6% |
| Load event | 1312 ms | 1806 ms | 494 ms | +37.7% |
| First contentful paint | 764 ms | 903 ms | 140 ms | +18.3% |
| Largest contentful paint | n/a | n/a | n/a | n/a |
| Time to video element | 18 ms | 31 ms | 12 ms | +67.6% |
| Time to playing | 40 ms | 32 ms | -9 ms | -22.2% |
| Video currentTime after wait | 11.14 s | 11.90 s | 0.76 s | +6.8% |
| Total run time | 17014 ms | 19640 ms | 2626 ms | +15.4% |

## Per-Run Timing

### no_blocker

| Run | DOMContentLoaded | Load | Video element | Playing | Video currentTime after wait | Anti-adblock text | Notes |
|---:|---:|---:|---:|---:|---:|---|---|
| 1 | 1179 ms | 1228 ms | 14 ms | 117 ms | 11.08 s | False |  |
| 2 | 2266 ms | 2330 ms | 23 ms | 47 ms | 9.95 s | False |  |
| 3 | 1257 ms | 3617 ms | 9 ms | 6 ms | 13.87 s | False |  |
| 4 | 1625 ms | 1644 ms | 30 ms | 22 ms | 11.63 s | False |  |
| 5 | 1119 ms | 1180 ms | 84 ms | 42 ms | 11.15 s | False |  |
| 6 | 1126 ms | 1170 ms | 85 ms | 39 ms | 11.13 s | False |  |
| 7 | 998 ms | 1044 ms | 14 ms | 121 ms | 11.11 s | False |  |
| 8 | 1721 ms | 1742 ms | 31 ms | 19 ms | 11.68 s | False |  |
| 9 | 1199 ms | 1396 ms | 7 ms | 113 ms | 11.24 s | False |  |
| 10 | 1130 ms | 1189 ms | 3 ms | 21 ms | 11.03 s | False |  |

### ubo

| Run | DOMContentLoaded | Load | Video element | Playing | Video currentTime after wait | Anti-adblock text | Notes |
|---:|---:|---:|---:|---:|---:|---|---|
| 1 | 1696 ms | 1716 ms | 19 ms | 25 ms | 11.89 s | False | installed addon: uBlock0@raymondhill.net |
| 2 | 1913 ms | 1934 ms | 49 ms | 30 ms | 11.97 s | False | installed addon: uBlock0@raymondhill.net |
| 3 | 1694 ms | 1833 ms | 27 ms | 41 ms | 11.97 s | False | installed addon: uBlock0@raymondhill.net |
| 4 | 1495 ms | 1516 ms | 35 ms | 51 ms | 11.67 s | False | installed addon: uBlock0@raymondhill.net |
| 5 | 1551 ms | 1590 ms | 28 ms | 27 ms | 11.81 s | False | installed addon: uBlock0@raymondhill.net |
| 6 | 1436 ms | 1482 ms | 10 ms | 22 ms | 11.70 s | False | installed addon: uBlock0@raymondhill.net |
| 7 | 1941 ms | 1971 ms | 33 ms | 70 ms | 11.97 s | False | installed addon: uBlock0@raymondhill.net |
| 8 | 2103 ms | 2247 ms | 29 ms | 48 ms | 12.37 s | False | installed addon: uBlock0@raymondhill.net |
| 9 | 1895 ms | 1915 ms | 33 ms | 31 ms | 11.92 s | False | installed addon: uBlock0@raymondhill.net |
| 10 | 1627 ms | 1779 ms | 54 ms | 32 ms | 11.85 s | False | installed addon: uBlock0@raymondhill.net |

## Per-Profile Timing Stats

### no_blocker

| Metric | Values | Min | Median | Mean | Max | Stdev |
|---|---|---:|---:|---:|---:|---:|
| DOMContentLoaded | `1257 ms, 1199 ms, 1179 ms, 1721 ms, 1130 ms, 2266 ms, 998 ms, 1625 ms, 1119 ms, 1126 ms` | 998 ms | 1189 ms | 1362 ms | 2266 ms | 393 ms |
| Load event | `3617 ms, 1396 ms, 1228 ms, 1742 ms, 1189 ms, 2330 ms, 1044 ms, 1644 ms, 1180 ms, 1170 ms` | 1044 ms | 1312 ms | 1654 ms | 3617 ms | 790 ms |
| First contentful paint | `665 ms, 834 ms, 798 ms, 1027 ms, 776 ms, 699 ms, 609 ms, 952 ms, 739 ms, 751 ms` | 609 ms | 764 ms | 785 ms | 1027 ms | 127 ms |
| Largest contentful paint | `n/a, n/a, n/a, n/a, n/a, n/a, n/a, n/a, n/a, n/a` | n/a | n/a | n/a | n/a | n/a |
| Time to video element | `9 ms, 7 ms, 14 ms, 31 ms, 3 ms, 23 ms, 14 ms, 30 ms, 84 ms, 85 ms` | 3 ms | 18 ms | 30 ms | 85 ms | 30 ms |
| Time to playing | `6 ms, 113 ms, 117 ms, 19 ms, 21 ms, 47 ms, 121 ms, 22 ms, 42 ms, 39 ms` | 6 ms | 40 ms | 55 ms | 121 ms | 45 ms |
| Video currentTime after wait | `13.87 s, 11.24 s, 11.08 s, 11.68 s, 11.03 s, 9.95 s, 11.11 s, 11.63 s, 11.15 s, 11.13 s` | 9.95 s | 11.14 s | 11.39 s | 13.87 s | 0.99 s |
| Total run time | `19889 ms, 17131 ms, 17062 ms, 18381 ms, 16965 ms, 16094 ms, 16643 ms, 18248 ms, 16948 ms, 16642 ms` | 16094 ms | 17014 ms | 17400 ms | 19889 ms | 1121 ms |

### ubo

| Metric | Values | Min | Median | Mean | Max | Stdev |
|---|---|---:|---:|---:|---:|---:|
| DOMContentLoaded | `1551 ms, 1627 ms, 1436 ms, 1895 ms, 1941 ms, 1694 ms, 1913 ms, 2103 ms, 1495 ms, 1696 ms` | 1436 ms | 1695 ms | 1735 ms | 2103 ms | 219 ms |
| Load event | `1590 ms, 1779 ms, 1482 ms, 1915 ms, 1971 ms, 1833 ms, 1934 ms, 2247 ms, 1516 ms, 1716 ms` | 1482 ms | 1806 ms | 1798 ms | 2247 ms | 234 ms |
| First contentful paint | `848 ms, 961 ms, 797 ms, 1040 ms, 1078 ms, 883 ms, 1010 ms, 923 ms, 860 ms, 826 ms` | 797 ms | 903 ms | 923 ms | 1078 ms | 96 ms |
| Largest contentful paint | `n/a, n/a, n/a, n/a, n/a, n/a, n/a, n/a, n/a, n/a` | n/a | n/a | n/a | n/a | n/a |
| Time to video element | `28 ms, 54 ms, 10 ms, 33 ms, 33 ms, 27 ms, 49 ms, 29 ms, 35 ms, 19 ms` | 10 ms | 31 ms | 32 ms | 54 ms | 13 ms |
| Time to playing | `27 ms, 32 ms, 22 ms, 31 ms, 70 ms, 41 ms, 30 ms, 48 ms, 51 ms, 25 ms` | 22 ms | 32 ms | 38 ms | 70 ms | 15 ms |
| Video currentTime after wait | `11.81 s, 11.85 s, 11.70 s, 11.92 s, 11.97 s, 11.97 s, 11.97 s, 12.37 s, 11.67 s, 11.89 s` | 11.67 s | 11.90 s | 11.91 s | 12.37 s | 0.19 s |
| Total run time | `19397 ms, 19538 ms, 19277 ms, 19755 ms, 19742 ms, 19779 ms, 19929 ms, 20235 ms, 19404 ms, 19411 ms` | 19277 ms | 19640 ms | 19647 ms | 20235 ms | 296 ms |

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

Raw JSON and screenshots live under `runs/20260522_172015_utc`.
Machine-readable summary: `runs/20260522_172015_utc/summary.json`.

Careful wording for publication: this run shows a repeatable playback-start delay under this exact Firefox/Selenium/uBO setup. It does not prove every browser, account state, region, network, or uBO version gets the same delay.
