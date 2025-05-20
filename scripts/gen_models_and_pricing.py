import os
import requests
from pathlib import Path
import sys

docs_dir = Path(__file__).parent.parent / "docs"
modelos_md = docs_dir / "modelos.md"
pricings_md = docs_dir / "pricings.md"

API_URL = "https://api.gradientesur.com/functions/v1/models"
API_KEY = os.environ.get("GRADIENTESUR_API_KEY")

if not API_KEY:
    print("Error: GRADIENTESUR_API_KEY environment variable not set.", file=sys.stderr)
    sys.exit(1)

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

resp = requests.get(API_URL, headers=headers)
resp.raise_for_status()
data = resp.json()["data"]

def make_modelos_md(models):
    content = [
        "# Modelos Disponibles",
        "",
        "Consultá los modelos disponibles también usando el endpoint `/functions/v1/models`.",
        "",
        "| Modelo | Descripción |",
        "|--------------------------------------------|----------------------------------------------------------------|"
    ]
    for m in models:
        content.append(f"| {m['name']} | {m['description']} |")
    return "\n".join(content) + "\n"

def make_pricings_md(models):
    # Group models by type for each section
    sections = [
        {
            "title": "Texto",
            "types": ["text"],
            "columns": ["Modelo", "Precio de entrada por 1M tokens", "Precio de salida por 1M tokens"],
            "rows": []
        },
        {
            "title": "Visión",
            "types": ["vision", "image"],
            "columns": ["Modelo", "Precio de entrada por 1M tokens", "Precio de salida por 1M tokens"],
            "rows": []
        },
        {
            "title": "Audio",
            "types": ["audio"],
            "columns": ["Modelo", "Precio por segundo de entrada", "Precio por segundo de salida"],
            "rows": []
        },
        {
            "title": "Embeddings",
            "types": ["embedding", "embeddings"],
            "columns": ["Modelo", "Precio por token de entrada"],
            "rows": []
        }
    ]

    # Assign models to sections
    for m in models:
        mtype = m.get("type", "").lower()
        p = m.get("pricing", {})
        for section in sections:
            if mtype in section["types"]:
                if section["title"] == "Texto" or section["title"] == "Visión":
                    section["rows"].append([
                        m["name"],
                        p.get("input", "$X.XX"),
                        p.get("output", "$X.XX")
                    ])
                elif section["title"] == "Audio":
                    section["rows"].append([
                        m["name"],
                        p.get("input", "$X.XX"),
                        p.get("output", "-")
                    ])
                elif section["title"] == "Embeddings":
                    section["rows"].append([
                        m["name"],
                        p.get("input", "$X.XX")
                    ])
                break

    content = ["# Precios", ""]
    for section in sections:
        content.append("")
        content.append(f"## {section['title']}")
        # Table header
        header = "| " + " | ".join(section["columns"]) + " |"
        sep = "|" + "|".join(["-" * (len(col) + 2) for col in section["columns"]]) + "|"
        content.append(header)
        content.append(sep)
        # Table rows
        for row_data in section["rows"]:
            content.append("| " + " | ".join(row_data) + " |")
        if not section["rows"]:
            # Add a placeholder row if no models for this section
            content.append("| - |" + " |" * (len(section["columns"]) - 1))
    content.append("")
    content.append("---")
    return "\n".join(content) + "\n"

modelos_md.write_text(make_modelos_md(data), encoding="utf-8")
pricings_md.write_text(make_pricings_md(data), encoding="utf-8")

print("modelos.md y pricings.md actualizados correctamente.")
