import importlib.util
from pathlib import Path

ROOT = Path(__file__).parents[1]


def load_module(name: str, relative: str):
    path = ROOT / relative
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


def test_mlops_manifest_contract():
    module = load_module("mlops_manifest", "skills/mlops-ai-operations/scripts/validate_model_manifest.py")
    valid = {
        "model_name": "classifier",
        "version": "1.0.0",
        "source_commit": "0123456789abcdef0123456789abcdef01234567",
        "dataset_digest": "sha256:" + "a" * 64,
        "metrics": {"f1": 0.9},
        "risk_owner": "ml-platform",
        "approved_for": "staging",
    }
    assert module.validate(valid) == []
    invalid = dict(valid, approved_for="unknown")
    assert module.validate(invalid)


def test_cloud_native_workload_contract():
    module = load_module("cloud_profile", "skills/cloud-native-security/scripts/validate_workload_profile.py")
    valid = {
        "namespace": "prod",
        "service_account": "api",
        "run_as_non_root": True,
        "allow_privilege_escalation": False,
        "capabilities_drop": ["ALL"],
        "seccomp_profile": "RuntimeDefault",
        "image_digest": "sha256:" + "b" * 64,
    }
    assert module.validate(valid) == []
    invalid = dict(valid, allow_privilege_escalation=True)
    assert module.validate(invalid)


def test_low_code_solution_contract():
    module = load_module("low_code_manifest", "skills/low-code-no-code-engineering/scripts/validate_solution_manifest.py")
    valid = {
        "solution_name": "member-onboarding",
        "solution_version": "1.0.0",
        "business_owner": "operations",
        "technical_owner": "platform",
        "data_classification": "internal",
        "connectors": ["Dataverse"],
        "dlp_reviewed": True,
        "environment_strategy": ["development", "test", "production"],
        "source_control_path": "src/member-onboarding",
    }
    assert module.validate(valid) == []
    invalid = dict(valid, dlp_reviewed=False)
    assert module.validate(invalid)


def test_slo_manifest_contract():
    module = load_module("slo_manifest", "skills/automated-sre-observability/scripts/validate_slo_manifest.py")
    valid = {
        "service_name": "checkout-api",
        "sli_type": "availability",
        "slo_target": 99.9,
        "measurement_window_days": 28,
        "error_budget_policy": "Feature-Release-Freeze bei Budgetverbrauch > 80%",
        "burn_rate_alerting": [
            {"window_hours": 1, "threshold_multiplier": 14.4, "severity": "page"},
            {"window_hours": 6, "threshold_multiplier": 6, "severity": "ticket"},
        ],
        "escalation_owner": "checkout-oncall",
        "runbook_url": "https://runbooks.internal/checkout-api-availability",
    }
    assert module.validate(valid) == []
    invalid = dict(valid, slo_target=100)
    assert module.validate(invalid)


def test_finops_cost_guardrail_contract():
    module = load_module("cost_guardrail", "skills/finops-cloud-governance/scripts/validate_cost_guardrail.py")
    valid = {
        "cost_center": "platform-payments",
        "workload_name": "checkout-api",
        "monthly_budget_usd": 12000,
        "alert_thresholds_pct": [50, 80, 100],
        "required_tags": ["cost-center", "owner", "environment", "service"],
        "owner": "payments-platform-team",
        "commitment_strategy": "savings-plan",
        "anomaly_detection": True,
    }
    assert module.validate(valid) == []
    invalid = dict(valid, anomaly_detection=False)
    assert module.validate(invalid)


def test_agent_run_contract():
    module = load_module("agent_run_contract", "skills/agentic-ai-orchestration-governance/scripts/validate_agent_run_contract.py")
    valid = {
        "agent_name": "pr-triage-agent",
        "max_iterations": 40,
        "max_tool_calls": 120,
        "context_budget_tokens": 150000,
        "tool_scope": ["github.read_pr", "github.comment", "ci.read_logs"],
        "kill_switch": True,
        "human_escalation_trigger": "vor jedem Force-Push, Merge oder externen Kommentar an Dritte",
        "cost_ceiling_usd": 5.0,
    }
    assert module.validate(valid) == []
    invalid = dict(valid, tool_scope=["*"])
    assert module.validate(invalid)
    unbounded = dict(valid, max_iterations=100000)
    assert module.validate(unbounded)
