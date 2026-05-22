# Adblock Diff Probe: rickroll_youtube

Target: `https://www.youtube.com/watch?v=Abva_f5giqg`
Run directory: `runs/20260522_173448_utc`
Summary JSON: `runs/20260522_173448_utc/summary.json`

## Verdict

Possible anti-adblock behavior: **not proven from this run**

- No timing/text signal crossed the configured threshold.

Interpretation: compare playback timing separately from page-load timing. A large `time_to_playing` delta with a small `time_to_video_element` delta means the page produced a video element quickly, but playback was delayed.

## Median Comparison

| Metric | No blocker median | uBO median | Delta | Percent change |
|---|---:|---:|---:|---:|
| DOMContentLoaded | 1868 ms | 1940 ms | 71 ms | +3.8% |
| Load event | 1912 ms | 1980 ms | 68 ms | +3.6% |
| First contentful paint | 826 ms | 1048 ms | 222 ms | +26.8% |
| Largest contentful paint | n/a | n/a | n/a | n/a |
| Time to video element | 54 ms | 9 ms | -45 ms | -83.3% |
| Time to playing | 20 ms | 24 ms | 4 ms | +19.5% |
| Video currentTime after wait | 9.78 s | 1.67 s | -8.11 s | -82.9% |
| Total run time | 15768 ms | 18038 ms | 2270 ms | +14.4% |

## Per-Run Timing

### no_blocker

| Run | DOMContentLoaded | Load | Video element | Playing | Video currentTime after wait | Anti-adblock text | Notes |
|---:|---:|---:|---:|---:|---:|---|---|
| 1 | 1842 ms | 1892 ms | 10 ms | 7 ms | 9.72 s | False |  |
| 2 | 2047 ms | 2077 ms | 29 ms | 12 ms | 9.50 s | False |  |
| 3 | 1951 ms | 1983 ms | 89 ms | 8 ms | 9.80 s | False |  |
| 4 | 1815 ms | 1866 ms | 4 ms | 23 ms | 9.76 s | False |  |
| 5 | 1730 ms | 1760 ms | 86 ms | 20 ms | 9.97 s | False |  |
| 6 | 1895 ms | 1932 ms | 83 ms | 23 ms | 9.83 s | False |  |
| 7 | 2225 ms | 2256 ms | 92 ms | 21 ms | 9.72 s | False |  |
| 8 | 1584 ms | 1612 ms | 3 ms | 88 ms | 11.68 s | False |  |
| 9 | 1979 ms | 2014 ms | 79 ms | 17 ms | 9.53 s | False |  |
| 10 | 1518 ms | 1548 ms | 12 ms | 519 ms | 11.53 s | False |  |

### ubo

| Run | DOMContentLoaded | Load | Video element | Playing | Video currentTime after wait | Anti-adblock text | Notes |
|---:|---:|---:|---:|---:|---:|---|---|
| 1 | 1947 ms | 1987 ms | 11 ms | 27 ms | 1.87 s | False | installed addon: uBlock0@raymondhill.net |
| 2 | 2025 ms | 2058 ms | 26 ms | 10 ms | 5.68 s | False | installed addon: uBlock0@raymondhill.net |
| 3 | 1977 ms | 2148 ms | 9 ms | 25 ms | 1.66 s | False | installed addon: uBlock0@raymondhill.net |
| 4 | 2201 ms | 2238 ms | 2 ms | 20 ms | 1.62 s | False | installed addon: uBlock0@raymondhill.net |
| 5 | 1775 ms | 1829 ms | 8 ms | 3592 ms | 11.09 s | False | installed addon: uBlock0@raymondhill.net |
| 6 | 1823 ms | 1872 ms | 9 ms | 37 ms | 1.58 s | False | installed addon: uBlock0@raymondhill.net |
| 7 | 1886 ms | 1925 ms | 22 ms | 25 ms | 1.67 s | False | installed addon: uBlock0@raymondhill.net |
| 8 | 1950 ms | 1988 ms | 3 ms | 17 ms | 1.72 s | False | installed addon: uBlock0@raymondhill.net |
| 9 | 1932 ms | 1973 ms | 3 ms | 18 ms | 1.54 s | False | installed addon: uBlock0@raymondhill.net |
| 10 | 1926 ms | 1974 ms | 10 ms | 24 ms | 1.67 s | False | installed addon: uBlock0@raymondhill.net |

## Per-Profile Timing Stats

### no_blocker

| Metric | Values | Min | Median | Mean | Max | Stdev |
|---|---|---:|---:|---:|---:|---:|
| DOMContentLoaded | `1518 ms, 1842 ms, 1584 ms, 1979 ms, 2047 ms, 2225 ms, 1895 ms, 1815 ms, 1951 ms, 1730 ms` | 1518 ms | 1868 ms | 1859 ms | 2225 ms | 212 ms |
| Load event | `1548 ms, 1892 ms, 1612 ms, 2014 ms, 2077 ms, 2256 ms, 1932 ms, 1866 ms, 1983 ms, 1760 ms` | 1548 ms | 1912 ms | 1894 ms | 2256 ms | 212 ms |
| First contentful paint | `958 ms, 712 ms, 937 ms, 745 ms, 851 ms, 1216 ms, 1267 ms, 802 ms, 795 ms, 725 ms` | 712 ms | 826 ms | 901 ms | 1267 ms | 198 ms |
| Largest contentful paint | `n/a, n/a, n/a, n/a, n/a, n/a, n/a, n/a, n/a, n/a` | n/a | n/a | n/a | n/a | n/a |
| Time to video element | `12 ms, 10 ms, 3 ms, 79 ms, 29 ms, 92 ms, 83 ms, 4 ms, 89 ms, 86 ms` | 3 ms | 54 ms | 49 ms | 92 ms | 40 ms |
| Time to playing | `519 ms, 7 ms, 88 ms, 17 ms, 12 ms, 21 ms, 23 ms, 23 ms, 8 ms, 20 ms` | 7 ms | 20 ms | 74 ms | 519 ms | 158 ms |
| Video currentTime after wait | `11.53 s, 9.72 s, 11.68 s, 9.53 s, 9.50 s, 9.72 s, 9.83 s, 9.76 s, 9.80 s, 9.97 s` | 9.50 s | 9.78 s | 10.10 s | 11.68 s | 0.80 s |
| Total run time | `17813 ms, 15624 ms, 17418 ms, 15754 ms, 15840 ms, 16028 ms, 15730 ms, 15655 ms, 15783 ms, 15604 ms` | 15604 ms | 15768 ms | 16125 ms | 17813 ms | 800 ms |

### ubo

| Metric | Values | Min | Median | Mean | Max | Stdev |
|---|---|---:|---:|---:|---:|---:|
| DOMContentLoaded | `1775 ms, 2201 ms, 1886 ms, 1977 ms, 1932 ms, 1950 ms, 2025 ms, 1947 ms, 1926 ms, 1823 ms` | 1775 ms | 1940 ms | 1944 ms | 2201 ms | 116 ms |
| Load event | `1829 ms, 2238 ms, 1925 ms, 2148 ms, 1973 ms, 1988 ms, 2058 ms, 1987 ms, 1974 ms, 1872 ms` | 1829 ms | 1980 ms | 1999 ms | 2238 ms | 122 ms |
| First contentful paint | `1126 ms, 1089 ms, 1004 ms, 1079 ms, 1022 ms, 1023 ms, 1122 ms, 1073 ms, 1008 ms, 990 ms` | 990 ms | 1048 ms | 1054 ms | 1126 ms | 50 ms |
| Largest contentful paint | `n/a, n/a, n/a, n/a, n/a, n/a, n/a, n/a, n/a, n/a` | n/a | n/a | n/a | n/a | n/a |
| Time to video element | `8 ms, 2 ms, 22 ms, 9 ms, 3 ms, 3 ms, 26 ms, 11 ms, 10 ms, 9 ms` | 2 ms | 9 ms | 10 ms | 26 ms | 8 ms |
| Time to playing | `3592 ms, 20 ms, 25 ms, 25 ms, 18 ms, 17 ms, 10 ms, 27 ms, 24 ms, 37 ms` | 10 ms | 24 ms | 380 ms | 3592 ms | 1129 ms |
| Video currentTime after wait | `11.09 s, 1.62 s, 1.67 s, 1.66 s, 1.54 s, 1.72 s, 5.68 s, 1.87 s, 1.67 s, 1.58 s` | 1.54 s | 1.67 s | 3.01 s | 11.09 s | 3.11 s |
| Total run time | `23525 ms, 18164 ms, 17895 ms, 18092 ms, 17984 ms, 17891 ms, 18053 ms, 18023 ms, 17930 ms, 18062 ms` | 17891 ms | 18038 ms | 18562 ms | 23525 ms | 1746 ms |

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
| `target_url` | `https://www.youtube.com/watch?v=Abva_f5giqg` |
| `viewport` | `1280x720` |
| `headless` | `False` |
| `runs_per_profile` | `10` |
| `navigation_timeout_s` | `45` |
| `video_timeout_s` | `20` |
| `settle_seconds` | `10` |
| `ubo_xpi_supplied` | `True` |

## Raw Outputs

Raw JSON and screenshots live under `runs/20260522_173448_utc`.
Machine-readable summary: `runs/20260522_173448_utc/summary.json`.

Careful wording for publication: this run shows a repeatable playback-start delay under this exact Firefox/Selenium/uBO setup. It does not prove every browser, account state, region, network, or uBO version gets the same delay.
