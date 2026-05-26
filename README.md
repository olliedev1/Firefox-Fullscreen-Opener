# Firefox-Fullscreen-Opener

A lightweight tool to open any website in [Firefox](https://www.mozilla.org/firefox/) in **fullscreen (kiosk) mode** — ideal for digital signage, kiosk displays, or just distraction-free browsing.

---

## Requirements

| Requirement | Notes |
|-------------|-------|
| Python 3.6+ | Only the standard library is used — no extra packages needed |
| Firefox | Must be installed and available on `PATH` |

---

## Installation

```bash
git clone https://github.com/olliedev1/Firefox-Fullscreen-Opener.git
cd Firefox-Fullscreen-Opener
chmod +x open_fullscreen.sh
```

---

## Usage

### Python script (cross-platform)

```bash
python3 firefox_fullscreen_opener.py <url>
```

### Shell wrapper (Linux / macOS)

```bash
./open_fullscreen.sh <url>
```

### Arguments

| Argument | Description |
|----------|-------------|
| `url` | Website URL to open. A bare domain (e.g. `example.com`) is accepted — `https://` is prepended automatically. |
| `--no-kiosk` | Open in a regular Firefox window instead of kiosk mode. |

---

## Examples

```bash
# Open example.com in kiosk (full-screen, no browser chrome)
python3 firefox_fullscreen_opener.py https://example.com

# Bare domain — https:// is added automatically
python3 firefox_fullscreen_opener.py example.com

# Open in a normal new window (not kiosk mode)
python3 firefox_fullscreen_opener.py --no-kiosk https://example.com

# Using the shell wrapper
./open_fullscreen.sh https://example.com
```

---

## How it works

By default the tool launches Firefox with the `--kiosk` flag, which:

- Forces the browser into full-screen mode immediately.
- Hides the address bar, toolbars, and all browser chrome.
- Prevents the user from exiting full screen via the keyboard (use `Alt+F4` or `pkill firefox` to quit; the exact shortcut depends on your window manager/desktop environment).

Pass `--no-kiosk` if you only need a standard new window without the kiosk restrictions.
