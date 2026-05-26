#!/usr/bin/env python3
"""
Firefox Fullscreen Opener
Opens a specified website URL in Firefox using fullscreen (kiosk) mode.
"""

import argparse
import subprocess
import sys


def open_firefox_fullscreen(url: str, kiosk: bool = True) -> None:
    """
    Open the given URL in Firefox in fullscreen mode.

    Args:
        url:    The website URL to open.
        kiosk:  When True (default), use --kiosk for a true fullscreen
                experience with no browser chrome. When False, use
                --new-window and let the window manager handle sizing.

    Raises:
        SystemExit: If Firefox is not found or fails to launch.
    """
    if not url.startswith(("http://", "https://", "ftp://", "file://")):
        url = "https://" + url

    flag = "--kiosk" if kiosk else "--new-window"
    cmd = ["firefox", flag, url]

    try:
        subprocess.Popen(cmd)
    except FileNotFoundError:
        print(
            "Error: Firefox was not found. "
            "Please install Firefox and ensure it is on your PATH.",
            file=sys.stderr,
        )
        sys.exit(1)
    except OSError as exc:
        print(f"Error: Failed to launch Firefox: {exc}", file=sys.stderr)
        sys.exit(1)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="firefox_fullscreen_opener",
        description="Open a website in Firefox in fullscreen mode.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
examples:
  %(prog)s https://example.com
  %(prog)s example.com          # https:// prefix is added automatically
  %(prog)s --no-kiosk https://example.com
        """,
    )
    parser.add_argument(
        "url",
        help="The URL (or bare domain) of the website to open.",
    )
    parser.add_argument(
        "--no-kiosk",
        dest="kiosk",
        action="store_false",
        default=True,
        help=(
            "Open in a regular new window instead of kiosk mode. "
            "Kiosk mode hides the browser chrome and forces full screen."
        ),
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    open_firefox_fullscreen(args.url, kiosk=args.kiosk)


if __name__ == "__main__":
    main()
