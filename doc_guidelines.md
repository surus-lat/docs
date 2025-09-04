# Documentation Guidelines

Guidelines for writing clean, developer-focused API documentation.

## Writing Style

### Tone
- **Direct and technical** - No marketing language or sales-y phrases
- **Minimalistic** - Remove unnecessary adjectives and fluff
- **Factual** - State capabilities without hype
- **Professional** - Avoid emojis, exclamation points, and casual language

### Examples
```
❌ "Perfecto para crear asistentes de voz, audiolibros o contenido accesible"
✅ "Convierte texto en audio"

❌ "El modelo de transcripción más avanzado de NVIDIA"  
✅ "Modelo de transcripción de NVIDIA"

❌ "¡Transcribe cualquier archivo de audio en solo 3 líneas de código!"
✅ "Convierte archivos de audio en texto"
```

## Document Structure

### Title and Description
- Use clear, functional titles
- Brief, direct description of what the endpoint does
- No marketing promises or superlatives

```markdown
# Audio Transcriptions

Convierte archivos de audio en texto. Es útil para transcribir grabaciones, entrevistas, etc.
```

### Main Sections (## Level)
Organize by functionality, not by complexity:

```markdown
## Solicitud
### Modelo: [model-name]
### Modelo: [alternative-model] (if applicable)

## Parámetros extra (if needed)
```

### Model Sections
Each model gets its own subsection with:

1. **Brief description** - What it does, key capabilities
2. **Code examples** - Python first, then JavaScript, then cURL
3. **Parameters** - Only if model-specific
4. **Advanced examples** - Within the same section

```markdown
### Modelo: nvidia/canary-1b-v2 (Canary)

Brief description of capabilities.

=== "Python"
    ```python
    # Clean, copy-paste ready code
    ```

=== "JavaScript" 
    ```javascript
    // Clean, copy-paste ready code
    ```

=== "cURL"
    ```bash
    # Clean, copy-paste ready code
    ```
```

## Code Examples

### Order
Always follow this order:
1. **Python** - Most common for developers
2. **JavaScript** - Second most common
3. **cURL** - For testing and debugging

### Python Style
```python
import requests

SURUS_API_KEY = "tu_clave_api"
API_URL = "https://api.surus.dev/functions/v1/endpoint"
headers = {"Authorization": "Bearer " + SURUS_API_KEY}

# Clear, minimal example
with open('file.wav', 'rb') as f:
    files = {'file': f}
    data = {'model': 'model-name'}
    response = requests.post(API_URL, headers=headers, data=data, files=files)
    print(response.json())
```

### JavaScript Style
```javascript
const SURUS_API_KEY = "tu_clave_api";
const API_URL = 'https://api.surus.dev/functions/v1/endpoint';
const formData = new FormData();
formData.append('model', 'model-name');
formData.append('file', fileInput.files[0]);

fetch(API_URL, {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer ' + SURUS_API_KEY
  },
  body: formData
})
.then(res => res.json())
.then(data => console.log(data));
```

### cURL Style
```bash
curl -X POST https://api.surus.dev/functions/v1/endpoint \
  -H "Authorization: Bearer tu_clave_api" \
  -F "model=model-name" \
  -F "file=@file.wav"
```

## Content Organization

### Within Each Section
1. **Basic usage first** - Simplest working example
2. **Parameters** - Clear list with types and descriptions
3. **Response format** - Show expected output
4. **Advanced usage** - Complex examples within the same section

### Parameter Documentation
```markdown
### Parámetros

- `model`: `model-name` - Required model identifier
- `file`: Archivo de audio a transcribir
- `source_lang` (opcional): Idioma del audio (ej: `es`, `en`, `fr`)
- `target_lang` (opcional): Idioma de la transcripción (ej: `es`, `en`, `fr`)
```

### Response Examples
```markdown
### Respuesta

```json
{
  "text": "Hola, ¿cómo estás?"
}
```
```

## Advanced Examples

Keep advanced examples within their relevant sections, not in separate sections:

```markdown
### Traducción

Brief description of the advanced feature.

=== "Python"
    ```python
    # Advanced example code
    ```

=== "JavaScript"
    ```javascript
    // Advanced example code
    ```
```

## What to Avoid

- ❌ Marketing language ("amazing", "powerful", "cutting-edge")
- ❌ Exclamation points and emojis
- ❌ Lengthy explanations of obvious concepts
- ❌ Separate "Advanced" sections at the end
- ❌ Inconsistent parameter names between examples
- ❌ Code examples with excessive comments
- ❌ Promises about performance or quality

## What to Include

- ✅ Clear, working code examples
- ✅ Consistent variable names across examples
- ✅ Brief, factual descriptions
- ✅ Parameter types and requirements
- ✅ Expected response formats
- ✅ Model-specific capabilities
- ✅ Advanced usage within relevant sections