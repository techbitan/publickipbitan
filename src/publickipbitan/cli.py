"""Command line interface for publickipbitan."""

from __future__ import annotations

import argparse
import json
import sys

from .core import PublicIPError, get_public_ip_json


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="publickipbitan",
        description="Show your public internet IP address.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Show output in JSON format.",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=5.0,
        help="Timeout in seconds for each public IP service. Default: 5",
    )

    args = parser.parse_args(argv)

    try:
        data = get_public_ip_json(timeout=args.timeout)
    except PublicIPError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(data, indent=2))
    else:
        print(data["public_ip"])

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
