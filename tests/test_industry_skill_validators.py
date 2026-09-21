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
