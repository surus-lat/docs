# Chat Completions

Este endpoint te permite generar respuestas de texto basadas en una conversación. Puedes enviar una serie de mensajes y el modelo continuará la conversación.

=== "Python"
    ```python
    import requests

    GS_API_KEY= "tu_clave_api"
    API_URL = "https://api.gradientesur.com/functions/v1/chat/completions"
    headers = {"Authorization": "Bearer " + GS_API_KEY}

    data = {
        "model": "Qwen/Qwen3-1.7B",
        "messages": [{"role": "user", "content": "Hola, cómo estás?"}],
        "max_tokens": 200
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
            model: 'Qwen/Qwen3-1.7B',
            messages: [{ role: 'user', content: 'Hola, cómo estás?' }],
            max_tokens: 200
        })
    })
    .then(res => res.json())
    .then(data => {
        console.log("Full response:", JSON.stringify(data, null, 2));
        console.log("\nAI response:", data.choices[0].message.content);
    });
    ```

=== "cURL"
    ```bash
    curl -X POST https://api.gradientesur.com/functions/v1/chat/completions \
      -H "Authorization: Bearer tu_clave_api" \
      -H "Content-Type: application/json" \
      -d '{"model": "Qwen/Qwen3-1.7B", "messages": [{"role": "user", "content": "Hola, cómo estás?"}], "max_tokens": 200}'
    ```

## Ejemplo de respuesta:
```json
{
  "id": "chatcmpl-ec1e82a53ab04d20b5560ec4c6b1f16a",
  "object": "chat.completion",
  "created": 1748351434,
  "model": "Qwen/Qwen3-1.7B",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "reasoning_content": "\nOkay, the user said \"Hola, c\u00f3mo est\u00e1s?\" which is Spanish for \"Hello, how are you?\" I need to respond in a friendly and helpful way.\n\nFirst, I should acknowledge their greeting. Maybe say \"\u00a1Hola!\" to keep the conversation friendly. Then, I should mention that I'm doing well, but I should also invite them to ask questions. That way, they feel comfortable asking for help if needed.\n\nI should make sure the response is in Spanish, as the user started with Spanish. Let me check the grammar and flow. \"\u00a1Hola! Estoy bien, gracias. \u00bfC\u00f3mo est\u00e1s t\u00fa?\" That sounds good. Then add an emoji to keep it friendly. Maybe end with a question to encourage them to ask anything. \n\nI should also consider if there's any cultural nuance I need to be aware of. Since it's a simple greeting, probably not much, but it's good to keep the tone warm and approachable. Alright,",
        "content": "¡Hola! Estoy bien, gracias. ¿Cómo estás tú? 😊 Si tienes alguna pregunta o necesitas ayuda, ¡no dudes en decírmelo!",
        "tool_calls": []
      },
      "logprobs": null,
      "finish_reason": "stop",
      "stop_reason": null
    }
  ],
  "usage": {
    "prompt_tokens": 14,
    "total_tokens": 230,
    "completion_tokens": 216,
    "prompt_tokens_details": null
  },
  "prompt_logprobs": null
}
```

---

## Parámetros extra soportados

Podés enviar los siguientes parámetros adicionales en tu petición para controlar el comportamiento de la generación y el formato de la respuesta.

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

=== "Python"
    ```python
    import requests

    GS_API_KEY = "tu_clave_api"
    API_URL = "https://api.gradientesur.com/functions/v1/chat/completions"
    headers = {"Authorization": "Bearer " + GS_API_KEY}

    data = {
        "model": "Qwen/Qwen3-1.7B",
        "messages": [{"role": "user", "content": "Hola, cómo estás?"}],
        "max_tokens": 200,
        "top_k": 20,
        "repetition_penalty": 1.1,
        "guided_regex": ".*\\?$"
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
            model: 'Qwen/Qwen3-1.7B',
            messages: [{ role: 'user', content: 'Hola, cómo estás?' }],
            max_tokens: 200,
            top_k: 20,
            repetition_penalty: 1.1,
            guided_regex: '.*\\?$'
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
      -d '{"model": "Qwen/Qwen3-1.7B", "messages": [{"role": "user", "content": "Hola, cómo estás?"}], "max_tokens": 200, "top_k": 20, "repetition_penalty": 1.1, "guided_regex": ".*\\?$"}'
    ```

---