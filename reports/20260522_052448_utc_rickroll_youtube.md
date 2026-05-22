# Adblock Diff Probe: rickroll_youtube

Target: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
Run directory: `runs/20260522_052448_utc`

## Summary

Possible anti-adblock behavior: **not proven from this run**

## Median Metrics

| Metric | No blocker | uBO | Delta |
|---|---:|---:|---:|
| DOMContentLoaded | 1368 ms | 1307 ms | -61 ms |
| Load event | 1416 ms | 1365 ms | -51 ms |
| First contentful paint | 476 ms | 476 ms | 0 ms |
| Largest contentful paint | n/a | n/a | n/a |
| Time to video element | 80 ms | 36 ms | -44 ms |
| Time to playing | 109 ms | 92 ms | -17 ms |
| Video currentTime after wait | 11.82 | 11.72 | -0.10 |
| Requests | 193.00 | 193.00 | 0.00 |
| Failed requests | 11.00 | 11.00 | 0.00 |
| Third-party requests | 150.00 | 151.00 | 1.00 |
| Tracker-ish domains | 2.00 | 2.00 | 0.00 |
| Console errors | 9.00 | 9.00 | 0.00 |
| Console warnings | 7.00 | 5.00 | -2.00 |

## Network Diff

Median request delta with uBO: `0.00` (0.00%)

Domains only seen without blocker: `3`
- `rr1---sn-ntqe6nes.googlevideo.com`
- `rr2---sn-5ualdnsz.c.youtube.com`
- `rr3---sn-5hnednsz.googlevideo.com`

Domains only seen with uBO: `4`
- `lh3.googleusercontent.com`
- `rr1---sn-5uaeznyz.googlevideo.com`
- `rr4---sn-q4flrnle.googlevideo.com`
- `rr5---sn-q4fl6nd6.googlevideo.com`

## Tracker-ish Domains

No blocker:
- `googleads.g.doubleclick.net`
- `static.doubleclick.net`

uBO:
- `googleads.g.doubleclick.net`
- `static.doubleclick.net`

## Raw Outputs

JSON and screenshots live under `runs/20260522_052448_utc`.
