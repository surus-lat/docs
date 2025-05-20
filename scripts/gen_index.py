
import os
from pathlib import Path
import yaml

DOCS_DIR = Path(__file__).parent.parent / "docs"
INDEX_MD = DOCS_DIR / "index.md"

# Files to exclude from the index listing
default_exclude = {"index.md", ".DS_Store"}

def get_title(md_path):
    with open(md_path, encoding="utf-8") as f:
        for line in f:
            if line.strip().startswith("# "):
                return line.strip().lstrip("# ").strip()
    return md_path.stem.capitalize()

def main():
    # Parse mkdocs.yml to get nav order
    mkdocs_yml = Path(__file__).parent.parent / "mkdocs.yml"
    with open(mkdocs_yml, encoding="utf-8") as f:
        mkdocs = yaml.safe_load(f)
    nav = mkdocs.get("nav", [])

    # Flatten nav to get ordered list of md files
    def extract_md_files(nav_section):
        result = []
        for item in nav_section:
            if isinstance(item, dict):
                for v in item.values():
                    if isinstance(v, str) and v.endswith(".md"):
                        result.append(v)
                    elif isinstance(v, list):
                        result.extend(extract_md_files(v))
            elif isinstance(item, str) and item.endswith(".md"):
                result.append(item)
        return result

    ordered_files = extract_md_files(nav)
    # Only include files that exist and are not excluded
    files = [DOCS_DIR / f for f in ordered_files if (DOCS_DIR / f).exists() and f not in default_exclude]

    lines = [
        "# Documentación de la API de GradienteSur\n",
        "Bienvenido/a a la documentación oficial de la API de GradienteSur!\n",
        "Esta API ofrece modelos de IA compatibles con el formato de OpenAI, para que los integres de manera sencilla en todo tipo de tareas.\n",
        "\n## Índice\n"
    ]
    for f in files:
        title = get_title(f)
        lines.append(f"- [{title}]({f.name})")
    lines.append("\n---\n")
    with open(INDEX_MD, "w", encoding="utf-8") as out:
        out.write("\n".join(lines))

if __name__ == "__main__":
    main()
