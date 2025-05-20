import mkdocs_gen_files
from pathlib import Path

# Directory containing markdown files
DOCS_DIR = Path(mkdocs_gen_files.config.config['docs_dir'])

# Files to exclude from the index listing
default_exclude = {"index.md", ".DS_Store"}

def get_title(md_path):
    with open(md_path, encoding="utf-8") as f:
        for line in f:
            if line.strip().startswith("# "):
                return line.strip().lstrip("# ").strip()
    return md_path.stem.capitalize()

def main():
    files = [f for f in sorted(DOCS_DIR.glob("*.md")) if f.name not in default_exclude]
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
    mkdocs_gen_files.open("index.md", "w").write("\n".join(lines))

main()
