# Adblock Diff Probe: rickroll_youtube

Target: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
Run directory: `runs/20260522_053546_utc`

## Summary

Possible anti-adblock behavior: **YES**

- uBO median time-to-playing was 11291 ms slower

## Median Metrics

| Metric | No blocker | uBO | Delta |
|---|---:|---:|---:|
| DOMContentLoaded | 908 ms | 1591 ms | 683 ms |
| Load event | 1006 ms | 1696 ms | 690 ms |
| First contentful paint | 532 ms | 1017 ms | 485 ms |
| Largest contentful paint | n/a | n/a | n/a |
| Time to video element | 12 ms | 18 ms | 6 ms |
| Time to playing | 618 ms | 11909 ms | 11291 ms |
| Video currentTime after wait | 11.64 | 11.02 | -0.61 |

## Detected Anti-Adblock Phrases

None detected in visible body text.

## Per-Run Details

### ubo

| Run | Time to playing | Video currentTime after wait | Anti-adblock text | Notes |
|---:|---:|---:|---|---|
| 1 | 11653 ms | 11.01 | False | installed addon: uBlock0@raymondhill.net |
| 2 | 11909 ms | 11.10 | False | installed addon: uBlock0@raymondhill.net |
| 3 | 12000 ms | 11.02 | False | installed addon: uBlock0@raymondhill.net |

### no_blocker

| Run | Time to playing | Video currentTime after wait | Anti-adblock text | Notes |
|---:|---:|---:|---|---|
| 1 | 618 ms | 11.64 | False |  |
| 2 | 639 ms | 11.64 | False |  |
| 3 | 75 ms | 11.05 | False |  |

## Raw Outputs

JSON and screenshots live under `runs/20260522_053546_utc`.
