# Adblock Diff Probe

Small Firefox/Selenium harness for measuring how a webpage behaves with and without an ad blocker.

The initial hardcoded target is the Rickroll YouTube video:

`https://www.youtube.com/watch?v=dQw4w9WgXcQ`

The point is not to bypass ads. The point is to collect repeatable timing evidence: page load timing, video element timing, actual playback timing, screenshots, JSON, and a markdown report.

## What it measures

For each profile/run:

- DOMContentLoaded timing
- load event timing
- first contentful paint
- largest contentful paint, when available
- time until a `<video>` element exists
- time until the video actually starts playing
- video `currentTime` after a fixed wait period
- visible anti-adblock text detection
- screenshot
- raw JSON result

The important distinction is:

- `time_to_video_element_ms`: the page created a video element
- `time_to_playing_ms`: the video actually began playback

If the video element appears quickly but playback is delayed, that is the interesting signal.

## Setup

```bash
mkdir -p ~/repos/adblock_diff_probe
cd ~/repos/adblock_diff_probe

python -m venv .venv
source .venv/bin/activate

pip install -U selenium
```

Selenium Manager should handle `geckodriver` automatically. You do not need a system `geckodriver` install if this works:

```bash
python - <<'PY'
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

opts = Options()
opts.add_argument("-headless")

driver = webdriver.Firefox(options=opts)
driver.get("https://example.com")
print(driver.title)
driver.quit()
PY
```

Expected output:

```text
Example Domain
```

## Get uBlock Origin Firefox XPI

```bash
mkdir -p extensions
cd extensions

python - <<'PY'
import json, urllib.request

url = "https://api.github.com/repos/gorhill/uBlock/releases/latest"
data = json.load(urllib.request.urlopen(url))

print(data["tag_name"])
for asset in data["assets"]:
    name = asset["name"]
    if name.endswith(".xpi") or "firefox" in name.lower():
        print(name, asset["browser_download_url"])
PY
```

Download the printed XPI URL:

```bash
wget -O ubo-firefox.xpi 'PASTE_XPI_URL_HERE'
```

Then go back to the repo root:

```bash
cd ..
```

## Run baseline only

```bash
python adblock_diff_probe.py --runs 3
```

This only runs the `no_blocker` profile. It is useful as a smoke test.

## Run comparison

```bash
python adblock_diff_probe.py --runs 3 --ubo-xpi extensions/ubo-firefox.xpi
```

Outputs:

```text
runs/<timestamp>/
  no_blocker/run_1.json
  no_blocker/run_1.png
  ubo/run_1.json
  ubo/run_1.png
  summary.json

reports/<timestamp>_rickroll_youtube.md
```

## Recommended test discipline

For a decent public post, do not rely on one run.

Use at least:

```bash
python adblock_diff_probe.py --runs 10 --ubo-xpi extensions/ubo-firefox.xpi
```

Better:

- run headful first, not headless
- avoid playing other video/network-heavy stuff during the test
- do not sign into YouTube for the first baseline
- record Firefox version
- record uBO version / XPI filename
- run multiple batches at different times
- include raw JSON and screenshots
- do not claim universal behavior from one machine

## Interpreting results

A strong result looks like this:

```text
No blocker median time-to-playing: 618 ms
uBO median time-to-playing: 11909 ms
Delta: 11291 ms
```

That does not automatically prove intent. It does prove that under this test setup, playback begins much later with uBO active.
