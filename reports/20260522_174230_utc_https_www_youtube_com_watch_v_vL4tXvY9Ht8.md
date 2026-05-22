# Adblock Diff Probe: rickroll_youtube

Target: `https://www.youtube.com/watch?v=vL4tXvY9Ht8`
Run directory: `runs/20260522_174230_utc`
Summary JSON: `runs/20260522_174230_utc/summary.json`

## Verdict

Possible anti-adblock behavior: **not proven from this run**

- No timing/text signal crossed the configured threshold.

Interpretation: compare playback timing separately from page-load timing. A large `time_to_playing` delta with a small `time_to_video_element` delta means the page produced a video element quickly, but playback was delayed.

## Median Comparison

| Metric | No blocker median | uBO median | Delta | Percent change |
|---|---:|---:|---:|---:|
| DOMContentLoaded | 1654 ms | 2029 ms | 374 ms | +22.6% |
| Load event | 1681 ms | 2102 ms | 422 ms | +25.1% |
| First contentful paint | 910 ms | 1054 ms | 143 ms | +15.7% |
| Largest contentful paint | n/a | n/a | n/a | n/a |
| Time to video element | 18 ms | 9 ms | -10 ms | -51.4% |
| Time to playing | 24 ms | 24 ms | -0 ms | -2.1% |
| Video currentTime after wait | 11.37 s | 11.50 s | 0.13 s | +1.1% |
| Total run time | 17268 ms | 19902 ms | 2634 ms | +15.3% |

## Per-Run Timing

### no_blocker

| Run | DOMContentLoaded | Load | Video element | Playing | Video currentTime after wait | Anti-adblock text | Notes |
|---:|---:|---:|---:|---:|---:|---|---|
| 1 | 1421 ms | 1439 ms | 39 ms | 21 ms | 11.62 s | False |  |
| 2 | 1970 ms | 1994 ms | 25 ms | 26 ms | 11.91 s | False |  |
| 3 | 1607 ms | 1626 ms | 34 ms | 22 ms | 11.69 s | False |  |
| 4 | 1945 ms | 2004 ms | 2 ms | 15 ms | 9.43 s | False |  |
| 5 | 1702 ms | 1746 ms | 2 ms | 72 ms | 11.80 s | False |  |
| 6 | 1101 ms | 1164 ms | 9 ms | 9 ms | 11.06 s | False |  |
| 7 | 1710 ms | 1736 ms | 2 ms | 32 ms | 11.81 s | False |  |
| 8 | 1367 ms | 1388 ms | 36 ms | 162 ms | 11.12 s | False |  |
| 9 | 2196 ms | 2267 ms | 20 ms | 8 ms | 9.87 s | False |  |
| 10 | 1149 ms | 1182 ms | 17 ms | 97 ms | 11.12 s | False |  |

### ubo

| Run | DOMContentLoaded | Load | Video element | Playing | Video currentTime after wait | Anti-adblock text | Notes |
|---:|---:|---:|---:|---:|---:|---|---|
| 1 | 2088 ms | 2168 ms | 2 ms | 23 ms | 10.02 s | False | installed addon: uBlock0@raymondhill.net |
| 2 | 2071 ms | 2227 ms | 9 ms | 8 ms | 12.19 s | False | installed addon: uBlock0@raymondhill.net |
| 3 | 1662 ms | 1700 ms | 15 ms | 24 ms | 11.84 s | False | installed addon: uBlock0@raymondhill.net |
| 4 | 1489 ms | 1528 ms | 47 ms | 158 ms | 11.15 s | False | installed addon: uBlock0@raymondhill.net |
| 5 | 2233 ms | 2256 ms | 13 ms | 27 ms | 12.24 s | False | installed addon: uBlock0@raymondhill.net |
| 6 | 1940 ms | 2053 ms | 6 ms | 26 ms | 11.98 s | False | installed addon: uBlock0@raymondhill.net |
| 7 | 2183 ms | 2271 ms | 9 ms | 14 ms | 10.00 s | False | installed addon: uBlock0@raymondhill.net |
| 8 | 2054 ms | 2108 ms | 12 ms | 21 ms | 12.14 s | False | installed addon: uBlock0@raymondhill.net |
| 9 | 2004 ms | 2097 ms | 3 ms | 9 ms | 9.75 s | False | installed addon: uBlock0@raymondhill.net |
| 10 | 1956 ms | 1992 ms | 4 ms | 1342 ms | 11.03 s | False | installed addon: uBlock0@raymondhill.net |

## Per-Profile Timing Stats

### no_blocker

| Metric | Values | Min | Median | Mean | Max | Stdev |
|---|---|---:|---:|---:|---:|---:|
| DOMContentLoaded | `1421 ms, 1101 ms, 1367 ms, 1702 ms, 1945 ms, 1149 ms, 1970 ms, 2196 ms, 1710 ms, 1607 ms` | 1101 ms | 1654 ms | 1617 ms | 2196 ms | 360 ms |
| Load event | `1439 ms, 1164 ms, 1388 ms, 1746 ms, 2004 ms, 1182 ms, 1994 ms, 2267 ms, 1736 ms, 1626 ms` | 1164 ms | 1681 ms | 1655 ms | 2267 ms | 367 ms |
| First contentful paint | `787 ms, 714 ms, 1276 ms, 932 ms, 791 ms, 764 ms, 1093 ms, 907 ms, 944 ms, 914 ms` | 714 ms | 910 ms | 912 ms | 1276 ms | 169 ms |
| Largest contentful paint | `n/a, n/a, n/a, n/a, n/a, n/a, n/a, n/a, n/a, n/a` | n/a | n/a | n/a | n/a | n/a |
| Time to video element | `39 ms, 9 ms, 36 ms, 2 ms, 2 ms, 17 ms, 25 ms, 20 ms, 2 ms, 34 ms` | 2 ms | 18 ms | 19 ms | 39 ms | 15 ms |
| Time to playing | `21 ms, 9 ms, 162 ms, 72 ms, 15 ms, 97 ms, 26 ms, 8 ms, 32 ms, 22 ms` | 8 ms | 24 ms | 46 ms | 162 ms | 50 ms |
| Video currentTime after wait | `11.62 s, 11.06 s, 11.12 s, 11.80 s, 9.43 s, 11.12 s, 11.91 s, 9.87 s, 11.81 s, 11.69 s` | 9.43 s | 11.37 s | 11.14 s | 11.91 s | 0.85 s |
| Total run time | `17029 ms, 17094 ms, 17337 ms, 17486 ms, 15903 ms, 17199 ms, 17886 ms, 16031 ms, 17826 ms, 17683 ms` | 15903 ms | 17268 ms | 17147 ms | 17886 ms | 688 ms |

### ubo

| Metric | Values | Min | Median | Mean | Max | Stdev |
|---|---|---:|---:|---:|---:|---:|
| DOMContentLoaded | `2004 ms, 1489 ms, 1662 ms, 2183 ms, 2088 ms, 1940 ms, 2233 ms, 1956 ms, 2054 ms, 2071 ms` | 1489 ms | 2029 ms | 1968 ms | 2233 ms | 230 ms |
| Load event | `2097 ms, 1528 ms, 1700 ms, 2271 ms, 2168 ms, 2053 ms, 2256 ms, 1992 ms, 2108 ms, 2227 ms` | 1528 ms | 2102 ms | 2040 ms | 2271 ms | 245 ms |
| First contentful paint | `1122 ms, 1485 ms, 855 ms, 1340 ms, 1172 ms, 1004 ms, 1097 ms, 1010 ms, 971 ms, 965 ms` | 855 ms | 1054 ms | 1102 ms | 1485 ms | 190 ms |
| Largest contentful paint | `n/a, n/a, n/a, n/a, n/a, n/a, n/a, n/a, n/a, n/a` | n/a | n/a | n/a | n/a | n/a |
| Time to video element | `3 ms, 47 ms, 15 ms, 9 ms, 2 ms, 6 ms, 13 ms, 4 ms, 12 ms, 9 ms` | 2 ms | 9 ms | 12 ms | 47 ms | 13 ms |
| Time to playing | `9 ms, 158 ms, 24 ms, 14 ms, 23 ms, 26 ms, 27 ms, 1342 ms, 21 ms, 8 ms` | 8 ms | 24 ms | 165 ms | 1342 ms | 416 ms |
| Video currentTime after wait | `9.75 s, 11.15 s, 11.84 s, 10.00 s, 10.02 s, 11.98 s, 12.24 s, 11.03 s, 12.14 s, 12.19 s` | 9.75 s | 11.50 s | 11.23 s | 12.24 s | 0.99 s |
| Total run time | `18120 ms, 20865 ms, 19722 ms, 18282 ms, 18106 ms, 20082 ms, 20496 ms, 19283 ms, 20240 ms, 20310 ms` | 18106 ms | 19902 ms | 19551 ms | 20865 ms | 1043 ms |

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
| `target_url` | `https://www.youtube.com/watch?v=vL4tXvY9Ht8` |
| `viewport` | `1280x720` |
| `headless` | `False` |
| `runs_per_profile` | `10` |
| `navigation_timeout_s` | `45` |
| `video_timeout_s` | `20` |
| `settle_seconds` | `10` |
| `ubo_xpi_supplied` | `True` |

## Raw Outputs

Raw JSON and screenshots live under `runs/20260522_174230_utc`.
Machine-readable summary: `runs/20260522_174230_utc/summary.json`.

Careful wording for publication: this run shows a repeatable playback-start delay under this exact Firefox/Selenium/uBO setup. It does not prove every browser, account state, region, network, or uBO version gets the same delay.
