import os
from pathlib import Path
import re

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

# New function to manually parse mkdocs.yml for nav order
def get_ordered_nav_files(mkdocs_yml_path):
    ordered_files = []
    try:
        with open(mkdocs_yml_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Warning: mkdocs.yml not found at {mkdocs_yml_path}")
        return [] # mkdocs.yml not found, return empty list

    in_nav_section = False
    nav_section_base_indent = -1 # Indentation of the "nav:" key itself

    for line_content in lines:
        stripped_line = line_content.lstrip()
        current_indent = len(line_content) - len(stripped_line)

        if stripped_line.startswith("nav:"):
            in_nav_section = True
            nav_section_base_indent = current_indent
            continue

        if in_nav_section:
            if current_indent <= nav_section_base_indent and \
               stripped_line and not stripped_line.startswith("#"):
                in_nav_section = False
                break 

            if current_indent > nav_section_base_indent:
                # Regex to find unquoted .md files after a colon (e.g., "Title: file.md")
                # Allows alphanumeric, '.', '/', '_', '-' in paths.
                match = re.search(r":\s*([A-Za-z0-9./_-]+\.md)", line_content)
                if match:
                    ordered_files.append(match.group(1))
    
    return ordered_files

def main():
    mkdocs_yml = Path(__file__).parent.parent / "mkdocs.yml"
    
    nav_file_paths = get_ordered_nav_files(mkdocs_yml)

    lines = [
        "# Documentación de la API de surus\n",
        "Bienvenido/a a la documentación oficial de la API de surus!\n",
        "Esta API ofrece modelos de IA compatibles con el formato de OpenAI, para que los integres rápida y fácilmente para todo tipo de tareas.\n",
        "\n## Índice\n"
    ]
    
    linked_files_count = 0
    if not nav_file_paths:
        print("Warning: No navigation paths found in mkdocs.yml or mkdocs.yml not parsed correctly.")

    for nav_path_str in nav_file_paths:
        # nav_path_str is relative to DOCS_DIR, e.g., "comenzando/autenticacion.md" or "index.md"
        if nav_path_str in default_exclude: # Excludes the main index.md from being listed in itself
            continue

        resolved_md_path = DOCS_DIR / nav_path_str
        if resolved_md_path.exists():
            title = get_title(resolved_md_path)
            # Use nav_path_str for the link, as it's already relative to DOCS_DIR
            lines.append(f"- [{title}]({nav_path_str})")
            linked_files_count += 1
        else:
            print(f"Warning: File '{resolved_md_path}' specified in nav not found.")

    lines.append("\n---\n")
    lines.append("## Contribuciones\n")
    lines.append("Te invitamos a contribuir a la documentación! Si quisieras hacerlo, crea un issue o pull request en nuestro [repositorio de GitHub](https://github.com/GradienteSur/docs).\n")
    
    with open(INDEX_MD, "w", encoding="utf-8") as out:
        out.write("\n".join(lines))

    if linked_files_count > 0:
        print(f"Successfully generated {INDEX_MD} with {linked_files_count} links.")
    else:
        print(f"Warning: {INDEX_MD} was generated, but no files were indexed. "
              "Check mkdocs.yml nav structure, file paths, and script logic if this is unexpected.")

if __name__ == "__main__":
    main()
