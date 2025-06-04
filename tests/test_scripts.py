import pytest
from pathlib import Path
import sys
import importlib.util

# Helper to import a script as a module
def import_script(script_path):
    spec = importlib.util.spec_from_file_location("module.name", script_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module

def test_index_md_exists():
    script = Path(__file__).parent.parent / "scripts" / "gen_index.py"
    docs_dir = Path(__file__).parent.parent / "docs"
    index_md = docs_dir / "index.md"
    # Run the script to generate index.md
    import_script(script)
    assert index_md.exists(), "index.md should be generated"
    content = index_md.read_text(encoding="utf-8")
    assert "# Documentación de la API de surus" in content
    assert "## Índice" in content

def test_modelos_and_pricings_md_exist():
    docs_dir = Path(__file__).parent.parent / "docs"
    modelos_md = docs_dir / "modelos.md"
    pricings_md = docs_dir / "pricings.md"
    # Set a dummy API key to avoid sys.exit(1)
    import os
    os.environ["SURUS_API_KEY"] = "dummy"
    # Patch requests.get to avoid real API call
    import types
    import requests
    def fake_get(*args, **kwargs):
        class FakeResp:
            def raise_for_status(self): pass
            def json(self):
                return {"data": [
                    {"name": "test-model", "description": "desc", "type": "text", "pricing": {"input": "$1.00", "output": "$2.00"}},
                    {"name": "audio-model", "description": "desc", "type": "audio", "pricing": {"input": "$0.10"}},
                    {"name": "embed-model", "description": "desc", "type": "embedding", "pricing": {"input": "$0.01"}}
                ]}
        return FakeResp()
    requests.get = fake_get
    assert modelos_md.exists(), "modelos.md should be generated"
    assert pricings_md.exists(), "pricings.md should be generated"
    modelos_content = modelos_md.read_text(encoding="utf-8")
    pricings_content = pricings_md.read_text(encoding="utf-8")
    assert "# Modelos Disponibles" in modelos_content
    assert "# Precios" in pricings_content
