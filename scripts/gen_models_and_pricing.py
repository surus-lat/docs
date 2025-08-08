import os
import sys
import requests
from pathlib import Path

def fetch_models_data():
    """Fetch models data from the API using environment variable API key."""
    api_key = os.getenv("SURUS_API_KEY")
    if not api_key:
        print("Error: SURUS_API_KEY environment variable not set")
        sys.exit(1)
    
    api_url = "https://api.surus.dev/functions/v1/models"
    headers = {"Authorization": f"Bearer {api_key}"}
    
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get("data", [])
    except requests.RequestException as e:
        print(f"Error fetching models data: {e}")
        sys.exit(1)

def generate_models_md(models_data):
    """Generate modelos.md content."""
    content = ["# Modelos Disponibles\n"]
    content.append("Consultá los modelos disponibles también usando el endpoint `/functions/v1/models`.\n")
    content.append("\n| Modelo | Descripción |\n")
    content.append("|--------|-------------|\n")
    
    for model in models_data:
        name = model.get("name", "N/A")
        description = model.get("description", "N/A")
        content.append(f"| {name} | {description} |\n")
    
    return "".join(content)

def generate_pricings_md(models_data):
    """Generate pricings.md content."""
    content = ["# Precios\n\n"]
    
    sections = [
        {
            "title": "Texto",
            "types": ["text"],
            "tasks": [],
            "columns": ["Modelo", "Precio de entrada por 1M tokens", "Precio de salida por 1M tokens"],
            "rows": []
        },
        {
            "title": "Visión",
            "types": ["vision", "image"],
            "tasks": [],
            "columns": ["Modelo", "Precio de entrada por 1M tokens", "Precio de salida por 1M tokens"],
            "rows": []
        },
        {
            "title": "Audio - Transcripción",
            "types": [],
            "tasks": ["speech_to_text"],
            "columns": ["Modelo", "Precio por minuto de entrada", "Precio por minuto de salida"],
            "rows": []
        },
        {
            "title": "Audio - Texto a Voz",
            "types": [],
            "tasks": ["text_to_speech"],
            "columns": ["Modelo", "Precio por segundo de entrada", "Precio por segundo de salida"],
            "rows": []
        },
        {
            "title": "Embeddings",
            "types": ["embedding", "embeddings"],
            "tasks": [],
            "columns": ["Modelo", "Precio por token de entrada"],
            "rows": []
        }
    ]
    
    def format_price(price):
        if price is not None and price != "":
            try:
                return str(float(price)).rstrip("0").rstrip(".") if "." in str(float(price)) else str(float(price))
            except (ValueError, TypeError):
                return str(price)
        return "-"
    
    # Categorize models
    for model in models_data:
        model_type = model.get("type", "").lower()
        model_task = model.get("task", "").lower()
        pricing = model.get("pricing", {})
        name = model.get("name", "N/A")
        
        # Skip models with both input and output pricing as 0
        input_price = pricing.get("input_price_per_million_tokens") or pricing.get("input")
        output_price = pricing.get("output_price_per_million_tokens") or pricing.get("output")
        if (input_price in [None, "0", "0.0", "0.00000000"] and 
            output_price in [None, "0", "0.0", "0.00000000"]):
            continue
        
        for section in sections:
            # For audio models, use task field
            if (section["tasks"] and model_task in section["tasks"]) or (section["types"] and model_type in section["types"]):
                if section["title"] in ["Texto", "Visión"]:
                    section["rows"].append([
                        name,
                        format_price(pricing.get("input_price_per_million_tokens") or pricing.get("input")),
                        format_price(pricing.get("output_price_per_million_tokens") or pricing.get("output"))
                    ])
                elif section["title"] == "Audio - Transcripción":
                    # Convert per second to per minute if needed
                    input_val = pricing.get("input_price_per_minute")
                    output_val = pricing.get("output_price_per_minute")
                    if not input_val and pricing.get("input"):
                        try:
                            input_val = str(float(pricing.get("input")) * 60)
                        except Exception:
                            input_val = pricing.get("input")
                    if not output_val and pricing.get("output"):
                        try:
                            output_val = str(float(pricing.get("output")) * 60)
                        except Exception:
                            output_val = pricing.get("output")
                    section["rows"].append([
                        name,
                        format_price(input_val),
                        format_price(output_val)
                    ])
                elif section["title"] == "Audio - Texto a Voz":
                    # Use per second pricing
                    section["rows"].append([
                        name,
                        format_price(pricing.get("input_price_per_second") or pricing.get("input")),
                        format_price(pricing.get("output_price_per_second") or pricing.get("output"))
                    ])
                elif section["title"] == "Embeddings":
                    section["rows"].append([
                        name,
                        format_price(pricing.get("input_price_per_token") or pricing.get("input"))
                    ])
                break
    
    # Generate markdown for each section
    for section in sections:
        content.append(f"## {section['title']}\n\n")
        
        # Table header
        header = "| " + " | ".join(section["columns"]) + " |\n"
        separator = "|" + "|".join(["-" * (len(col) + 2) for col in section["columns"]]) + "|\n"
        content.append(header)
        content.append(separator)
        
        # Table rows
        if section["rows"]:
            for row in section["rows"]:
                content.append("| " + " | ".join(row) + " |\n")
        else:
            # Empty row
            empty_row = "| " + " | ".join(["-"] * len(section["columns"])) + " |\n"
            content.append(empty_row)
        
        content.append("\n")
    
    content.append("---\n")
    return "".join(content)

def main():
    docs_dir = Path(__file__).parent.parent / "docs"
    models_file = docs_dir / "modelos.md"
    pricings_file = docs_dir / "pricings.md"
    
    print("Fetching models data from API...")
    models_data = fetch_models_data()
    print(f"{models_data}")
    
    print(f"Generating {models_file}...")
    models_content = generate_models_md(models_data)
    with open(models_file, "w", encoding="utf-8") as f:
        f.write(models_content)
    
    print(f"Generating {pricings_file}...")
    pricings_content = generate_pricings_md(models_data)
    with open(pricings_file, "w", encoding="utf-8") as f:
        f.write(pricings_content)
    
    print("Done!")

if __name__ == "__main__":
    main()