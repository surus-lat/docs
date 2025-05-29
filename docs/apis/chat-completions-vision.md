# Chat Completions con Imagen

Este endpoint extiende la funcionalidad de Chat Completions permitiendo incluir imágenes en la conversación. El modelo puede analizar o describir el contenido de las imágenes proporcionadas.

### Solicitud

=== "Python"
    ```python
    import requests

    GS_API_KEY = "tu_clave_api"
    API_URL = "https://api.gradientesur.com/functions/v1/chat/completions"
    headers = {"Authorization": "Bearer " + GS_API_KEY}

    data = {
        "model": "OpenGVLab/InternVL3-2B",
        "messages": [
            {"role": "user", "content": [
                {"type": "text", "text": "Qué hay en esta imagen?"},
                {"type": "image_url", "image_url": {"url": "https://i.imgur.com/IqAOn4t.jpeg"}}
            ]}
        ],
        "max_tokens": 50
    }

    response = requests.post(API_URL, headers=headers, json=data)
    print(response.json())
    ```

=== "JavaScript"
    ```javascript
    const GS_API_KEY = "tu_clave_api";
    const API_URL = 'https://api.gradientesur.com/functions/v1/chat/completions';
    fetch(API_URL, {
      method: 'POST',
      headers: {
        'Authorization': 'Bearer ' + GS_API_KEY,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        model: 'OpenGVLab/InternVL3-2B',
        messages: [
          { role: 'user', content: [
            { type: 'text', text: 'Qué hay en esta imagen?' },
            { type: 'image_url', image_url: { url: 'https://i.imgur.com/IqAOn4t.jpeg' } }
          ] }
        ],
        max_tokens: 50
      })
    })
    .then(res => res.json())
    .then(data => console.log(data));
    ```

=== "cURL"
    ```bash
    curl -X POST https://api.gradientesur.com/functions/v1/chat/completions \
      -H "Authorization: Bearer tu_clave_api" \
      -H "Content-Type: application/json" \
      -d '{"model": "OpenGVLab/InternVL3-2B", "messages": [{"role": "user", "content": [{"type": "text", "text": "Qué hay en esta imagen?"}, {"type": "image_url", "image_url": {"url": "https://i.imgur.com/IqAOn4t.jpeg"}}]}], "max_tokens": 50}'
    ```

### Respuesta:

```json
{
  "id": "chatcmpl-638c8ca8b3254905bcfb2265a616c5eb",
  "object": "chat.completion",
  "created": 1748352291,
  "model": "OpenGVLab/InternVL3-2B",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "reasoning_content": null,
        "content": "La imagen muestra la parte frontal de un ojo irritado. El ojo tiene un p\u00e1rpito rojo intenso y un rasgu\u00f1o negro. Las pozas visco\u00e9lasticas est\u00e1n visibles. Este efecto contribuye a",
        "tool_calls": []
      },
      "logprobs": null,
      "finish_reason": "length",
      "stop_reason": null
    }
  ],
  "usage": {
    "prompt_tokens": 1830,
    "total_tokens": 1880,
    "completion_tokens": 50,
    "prompt_tokens_details": null
  },
  "prompt_logprobs": null
}
```

---

## Parámetros extra

Podés enviar los siguientes parámetros adicionales para controlar el comportamiento de la generación y el formato de la respuesta.

### Parámetros de muestreo

- `use_beam_search` (`bool`, default: `False`): Usa búsqueda por haces para la generación.
- `top_k` (`int`, opcional): Limita la selección al top-k tokens más probables.
- `min_p` (`float`, opcional): Probabilidad mínima acumulada para la selección de tokens.
- `repetition_penalty` (`float`, opcional): Penaliza la repetición de tokens.
- `length_penalty` (`float`, default: `1.0`): Penaliza o favorece secuencias largas.
- `stop_token_ids` (`list[int]`, opcional): IDs de tokens donde detener la generación.
- `include_stop_str_in_output` (`bool`, default: `False`): Incluye el string de parada en la salida.
- `ignore_eos` (`bool`, default: `False`): Ignora el token de fin de secuencia.
- `min_tokens` (`int`, default: `0`): Mínimo de tokens a generar.
- `skip_special_tokens` (`bool`, default: `True`): Omite tokens especiales en la salida.
- `spaces_between_special_tokens` (`bool`, default: `True`): Añade espacios entre tokens especiales.
- `truncate_prompt_tokens` (`int`, opcional): Trunca el prompt a este número de tokens.
- `allowed_token_ids` (`list[int]`, opcional): Solo permite estos tokens en la generación.
- `prompt_logprobs` (`int`, opcional): Devuelve logprobs de los tokens del prompt.

### Parámetros adicionales

- `add_special_tokens` (`bool`, default: `True`): Añade tokens especiales al prompt.
- `response_format` (`dict`, opcional): Especifica el formato de salida (`{'type': 'json_object'}`, `{'type': 'json_schema'}` o `{'type': 'text'}`).
- `guided_json` (`str`/`dict`, opcional): Fuerza la salida a seguir un esquema JSON.
- `guided_regex` (`str`, opcional): Fuerza la salida a seguir un patrón regex.
- `guided_choice` (`list[str]`, opcional): La salida será exactamente una de las opciones.
- `guided_grammar` (`str`, opcional): Fuerza la salida a seguir una gramática libre de contexto.
- `guided_decoding_backend` (`str`, opcional): Backend de decodificación guiada (`'outlines'` o `'lm-format-enforcer'`).
- `guided_whitespace_pattern` (`str`, opcional): Patrón de espacios para decodificación guiada.
- `priority` (`int`, default: `0`): Prioridad de la petición (solo para modelos que lo soportan).
- `logits_processors` (`list`, opcional): Lista de procesadores de logits a aplicar durante el muestreo.
- `return_tokens_as_token_ids` (`bool`, opcional): Si se usa con `logprobs`, representa tokens como `token_id:{token_id}`.

#### Ejemplo de uso

=== "Python"
    ```python
    import requests

    GS_API_KEY = "tu_clave_api"
    API_URL = "https://api.gradientesur.com/functions/v1/chat/completions"
    headers = {"Authorization": "Bearer " + GS_API_KEY}

    data = {
        "model": "OpenGVLab/InternVL3-2B",
        "messages": [
            {"role": "user", "content": [
                {"type": "text", "text": "Describe la imagen."},
                {"type": "image_url", "image_url": {"url": "https://i.imgur.com/IqAOn4t.jpeg"}}
            ]}
        ],
        "max_tokens": 50,
        "top_k": 10,
        "guided_choice": ["Es un perro.", "Es un gato."]
    }

    response = requests.post(API_URL, headers=headers, json=data)
    print(response.json())
    ```

=== "JavaScript"
    ```javascript
    const GS_API_KEY = "tu_clave_api";
    const API_URL = 'https://api.gradientesur.com/functions/v1/chat/completions';
    fetch(API_URL, {
    method: 'POST',
    headers: {
        'Authorization': 'Bearer ' + GS_API_KEY,
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        model: 'OpenGVLab/InternVL3-2B',
        messages: [
        { role: 'user', content: [
            { type: 'text', text: 'Describe la imagen.' },
            { type: 'image_url', image_url: { url: 'https://i.imgur.com/IqAOn4t.jpeg' } }
        ]}
        ],
        max_tokens: 50,
        top_k: 10,
        guided_choice: ["Es un perro.", "Es un gato."]
    })
    })
    .then(res => res.json())
    .then(data => console.log(data));
    ```

=== "cURL"
    ```bash
    curl -X POST https://api.gradientesur.com/functions/v1/chat/completions \
    -H "Authorization: Bearer tu_clave_api" \
    -H "Content-Type: application/json" \
    -d '{"model": "OpenGVLab/InternVL3-2B", "messages": [{"role": "user", "content": [{"type": "text", "text": "Describe la imagen."}, {"type": "image_url", "image_url": {"url": "https://i.imgur.com/IqAOn4t.jpeg"}}]}], "max_tokens": 50, "top_k": 10, "guided_choice": ["Es un perro.", "Es un gato."]}'
    ```

---