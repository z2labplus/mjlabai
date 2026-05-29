#!/usr/bin/env python3
"""Test substitute for Akochan system.exe.

This file is not Akochan and does not implement Mahjong AI behavior. It only
emits fixed JSON so the local wrapper skeleton can be tested without storing
third-party source, binaries, params, weights, or build artifacts.
"""

from __future__ import annotations

import json
from pathlib import Path
import sys


def _legal_action(args: list[str]) -> int:
    if len(args) != 1:
        print("usage: fake_system_exe.py legal_action <json>", file=sys.stderr)
        return 2
    payload = json.loads(args[0])
    if payload.get("force_invalid_stdout"):
        print("not-json")
        return 0
    print(
        json.dumps(
            [
                {"actor": 0, "pai": "1s", "tsumogiri": True, "type": "dahai"},
                {"actor": 0, "pai": "1m", "tsumogiri": False, "type": "dahai"},
            ],
            separators=(",", ":"),
        )
    )
    return 0


def _mjai_log(args: list[str]) -> int:
    if len(args) != 3:
        print("usage: fake_system_exe.py mjai_log <log_path> <actor> <mode>", file=sys.stderr)
        return 2
    runtime_file = Path.cwd() / "fake_setup_mjai.json"
    if not runtime_file.exists():
        print(f"missing fake runtime file in cwd: {runtime_file}", file=sys.stderr)
        return 6
    log_path, actor, mode = args
    sample_name = Path(log_path).name
    records = [
        {
            "type": "start_game",
            "aka_flag": True,
            "kyoku_first": 0,
            "names": ["p0", "p1", "p2", "p3"],
            "fake_log_path": log_path,
            "actor": int(actor),
            "mode": int(mode),
            "cwd": str(Path.cwd()),
        },
        {
            "type": "end_kyoku",
            "actor": int(actor),
            "mode": int(mode),
            "cwd": str(Path.cwd()),
        },
    ]

    if "json_lines" in sample_name:
        for record in records:
            print(json.dumps(record, separators=(",", ":")))
        return 0

    if "concatenated" in sample_name:
        sys.stdout.write("".join(json.dumps(record, separators=(",", ":")) for record in records))
        return 0

    if "pretty_stream" in sample_name:
        sys.stdout.write("\n".join(json.dumps(record, indent=2) for record in records))
        return 0

    if "invalid_mixed" in sample_name:
        sys.stdout.write(json.dumps(records[0], separators=(",", ":")) + "\nnot-json")
        return 0

    print(
        json.dumps(
            records[0],
            separators=(",", ":"),
        )
    )
    return 0


def main() -> int:
    if len(sys.argv) < 2:
        print("missing command", file=sys.stderr)
        return 2
    command = sys.argv[1]
    if command == "legal_action":
        return _legal_action(sys.argv[2:])
    if command == "mjai_log":
        return _mjai_log(sys.argv[2:])
    print(f"forbidden fake command: {command}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
