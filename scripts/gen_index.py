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
            # If the current line is less or equally indented than "nav:" key,
            # and it's not empty or a comment, then nav section has ended.
            if current_indent <= nav_section_base_indent and \
               stripped_line and not stripped_line.startswith("#"):
                in_nav_section = False
                break # Stop processing lines for nav

            # Only consider lines that are more indented than "nav:"
            if current_indent > nav_section_base_indent:
                # Look for '.md' files, typically in quotes
                match = re.search(r"['\"]([^'\"]+\.md)['\"]", line_content)
                if match:
                    ordered_files.append(match.group(1))
    
    return ordered_files

def main():
    # Parse mkdocs.yml to get nav order
    mkdocs_yml = Path(__file__).parent.parent / "mkdocs.yml"
    
    # Get ordered list of md files from mkdocs.yml nav section
    # This replaces the yaml parsing and extract_md_files logic
    nav_file_paths = get_ordered_nav_files(mkdocs_yml)

    # Only include files that exist and are not excluded
    files = []
    for f_path_str in nav_file_paths:
        resolved_path = DOCS_DIR / f_path_str
        # Use f_path_str for exclusion check as default_exclude contains relative paths
        if resolved_path.exists() and f_path_str not in default_exclude:
            files.append(resolved_path)

    lines = [
        
        "# Documentación de la API de GradienteSur\n",
        "Bienvenido/a a la documentación oficial de la API de GradienteSur!\n",
        "Esta API ofrece modelos de IA compatibles con el formato de OpenAI, para que los integres rápida y fácilmente para todo tipo de tareas.\n",
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
