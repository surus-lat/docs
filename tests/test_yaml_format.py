import pytest
import yaml
from pathlib import Path

def get_yaml_files():
    base = Path(__file__).parent.parent
    return list(base.glob('*.yml')) + list(base.glob('*.yaml'))

def pytest_generate_tests(metafunc):
    if 'yaml_file' in metafunc.fixturenames:
        metafunc.parametrize('yaml_file', get_yaml_files())

def test_yaml_valid_format(yaml_file):
    """Test that all YAML files are valid and can be loaded."""
    with open(yaml_file, 'r', encoding='utf-8') as f:
        try:
            yaml.safe_load(f)
        except yaml.YAMLError as e:
            pytest.fail(f"YAML file {yaml_file} is invalid: {e}")
