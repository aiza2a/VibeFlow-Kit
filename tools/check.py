#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
PROJECT_JSON = ROOT / ".ai" / "project.json"
PROFILES = ROOT / ".ai" / "profiles"


def load_active_profile(explicit: str | None) -> str:
    if explicit:
        return explicit
    if PROJECT_JSON.exists():
        data = json.loads(PROJECT_JSON.read_text(encoding="utf-8"))
        name = data.get("active_profile")
        if name:
            return str(name)
    raise SystemExit("No active profile found. Run: python tools/vcflow.py init --profile <name>")


def load_profile(name: str) -> dict[str, Any]:
    path = PROFILES / f"{name}.json"
    if not path.exists():
        raise SystemExit(f"Profile not found: {name}")
    return json.loads(path.read_text(encoding="utf-8"))


def run_command(command: str) -> int:
    print(f"\n==> {command}")
    result = subprocess.run(command, shell=True, cwd=ROOT)
    return result.returncode


def main() -> None:
    parser = argparse.ArgumentParser(description="Run quality checks for active profile")
    parser.add_argument("--profile", default=None, help="override active profile")
    parser.add_argument("--include-format", action="store_true", help="also run format check/format command")
    args = parser.parse_args()

    profile_name = load_active_profile(args.profile)
    profile = load_profile(profile_name)
    commands = profile.get("commands", {})

    stages: list[tuple[str, list[str]]] = []
    if args.include_format and commands.get("format"):
        stages.append(("format", commands["format"]))
    for key in ["lint", "typecheck", "test"]:
        if commands.get(key):
            stages.append((key, commands[key]))

    failures = 0
    for stage_name, stage_cmds in stages:
        print(f"\n## Running stage: {stage_name}")
        for cmd in stage_cmds:
            code = run_command(cmd)
            if code != 0:
                failures += 1
                print(f"FAILED [{stage_name}] {cmd} -> exit code {code}")
                break

    if failures:
        raise SystemExit(1)
    print(f"\nAll checks passed for profile: {profile_name}")


if __name__ == "__main__":
    main()
