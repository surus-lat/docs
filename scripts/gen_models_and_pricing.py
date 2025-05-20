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
    lines = [
        "# Modelos Disponibles\n",
        "\nConsultá los modelos disponibles también usando el endpoint `/functions/v1/models`.\n\n",
        "\n| Modelo | Descripción |\n",
        "|--------------------------------------------|----------------------------------------------------------------|\n"
    ]
    for m in models:
        lines.append(f"| {m['name']} | {m['description']} |\n")
    return "\n".join(lines)

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

    lines = ["# Precios\n", "\n# TODO: Cargar dinámicamente de la db\n"]
    for section in sections:
        lines.append(f"\n## {section['title']}\n")
        # Table header
        header = "| " + " | ".join(section["columns"]) + " |"
        sep = "|" + "-" * (len(section["columns"][0]) + 2)
        sep = "|" + "|".join(["-" * (len(col) + 2) for col in section["columns"]]) + "|"
        lines.append(header)
        lines.append(sep)
        # Table rows
        for row in section["rows"]:
            lines.append("| " + " | ".join(row) + " |")
        if not section["rows"]:
            # Add a placeholder row if no models for this section
            lines.append("| - |" + " |" * (len(section["columns"]) - 1))
    lines.append("\n---")
    return "\n".join(lines)

modelos_md.write_text(make_modelos_md(data), encoding="utf-8")
pricings_md.write_text(make_pricings_md(data), encoding="utf-8")

print("modelos.md y pricings.md actualizados correctamente.")
