#!/usr/bin/env python3
"""Run script for The Room Dialogue API."""

import argparse
import os
from room_api import create_app


def main():
    parser = argparse.ArgumentParser(description="Run The Room Dialogue API server.")
    parser.add_argument(
        "--host",
        default=os.environ.get("HOST", "127.0.0.1"),
        help="Host interface to bind to (default: 127.0.0.1)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=int(os.environ.get("PORT", "5000")),
        help="Port to listen on (default: 5000)",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        default=os.environ.get("FLASK_DEBUG", "0").lower() in ("1", "true"),
        help="Enable Flask debug mode",
    )
    args = parser.parse_args()

    app = create_app()
    print(f"🎬 Starting The Room Dialogue API on http://{args.host}:{args.port}")
    print("👉 Try: curl http://127.0.0.1:5000/whos-the-client")
    app.run(host=args.host, port=args.port, debug=args.debug)


if __name__ == "__main__":
    main()
