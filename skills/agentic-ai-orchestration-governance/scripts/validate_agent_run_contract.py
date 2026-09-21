#!/usr/bin/env python3
"""Validate a provider-neutral autonomous agent run contract."""
import argparse
import json
import sys
from pathlib import Path

REQUIRED = {
    "agent_name",
    "max_iterations",
    "max_tool_calls",
    "context_budget_tokens",
    "tool_scope",
    "kill_switch",
    "human_escalation_trigger",
    "cost_ceiling_usd",
}
MAX_REASONABLE_ITERATIONS = 500
MAX_REASONABLE_TOOL_CALLS = 2000
MAX_REASONABLE_CONTEXT_TOKENS = 1_000_000


def _positive_int(value) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value > 0


def validate(data: dict) -> list[str]:
    errors = []
    missing = sorted(REQUIRED - data.keys())
    if missing:
        errors.append("missing fields: " + ", ".join(missing))

    max_iterations = data.get("max_iterations")
    if not _positive_int(max_iterations):
        errors.append("max_iterations must be a positive integer")
    elif max_iterations > MAX_REASONABLE_ITERATIONS:
        errors.append(f"max_iterations must not exceed {MAX_REASONABLE_ITERATIONS} without explicit override review")

    max_tool_calls = data.get("max_tool_calls")
    if not _positive_int(max_tool_calls):
        errors.append("max_tool_calls must be a positive integer")
    elif max_tool_calls > MAX_REASONABLE_TOOL_CALLS:
        errors.append(f"max_tool_calls must not exceed {MAX_REASONABLE_TOOL_CALLS} without explicit override review")

    context_budget = data.get("context_budget_tokens")
    if not _positive_int(context_budget):
        errors.append("context_budget_tokens must be a positive integer")
    elif context_budget > MAX_REASONABLE_CONTEXT_TOKENS:
        errors.append(f"context_budget_tokens must not exceed {MAX_REASONABLE_CONTEXT_TOKENS} (leave margin below the model limit)")

    tool_scope = data.get("tool_scope")
    if not isinstance(tool_scope, list) or not tool_scope:
        errors.append("tool_scope must be a non-empty list of explicitly named tools")
    elif any(str(t).strip() in {"*", "all", "any"} for t in tool_scope):
        errors.append("tool_scope must not use wildcard/all-tool grants")

    if data.get("kill_switch") is not True:
        errors.append("kill_switch must be true; every autonomous run needs a tested, externally reachable kill switch")

    if not str(data.get("human_escalation_trigger", "")).strip():
        errors.append("human_escalation_trigger must describe when the run stops for human confirmation")

    cost_ceiling = data.get("cost_ceiling_usd")
    if not isinstance(cost_ceiling, (int, float)) or isinstance(cost_ceiling, bool) or cost_ceiling <= 0:
        errors.append("cost_ceiling_usd must be a positive number")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"valid": False, "errors": [str(exc)]}))
        return 2
    errors = validate(data)
    print(json.dumps({"valid": not errors, "errors": errors}, indent=2))
    return 0 if not errors else 2


if __name__ == "__main__":
    sys.exit(main())
