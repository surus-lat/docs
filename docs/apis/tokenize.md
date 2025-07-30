# Tokenize & Detokenize

Este endpoint sirve para rápidamente convertir texto a tokens y viceversa. Le podemos pasar cualquier modelo de HuggingFace compatible con transformers.

- [Documentación oficial de tokenizers](https://huggingface.co/docs/transformers/main_classes/tokenizer)

---

## Tokenización

Convierte texto en una lista de tokens (IDs) usando el tokenizer especificado.

### Solicitud

=== "Python"
    ```python
    import requests

    API_URL = "https://api.surus.dev/functions/v1/tokenize"
    data = {
        "tokenizer": "Qwen/Qwen3-1.7B",
        "text": "Hola, cómo estás?"
    }
    response = requests.post(API_URL, json=data)
    print(response.json())
    ```

=== "cURL"
    ```bash
    curl -X POST https://api.surus.dev/functions/v1/tokenize \
      -H "Content-Type: application/json" \
      -d '{"tokenizer": "Qwen/Qwen3-1.7B", "text": "Hola, cómo estás?"}'
    ```

### Respuesta

```json
{
  "tokens": [68012,11,54896,1788,7061,30],
  "length": 6
}
```

---

## Detokenización

Convierte una lista de tokens (IDs) en texto usando el tokenizer especificado.

### Solicitud

=== "Python"
    ```python
    import requests

    API_URL = "https://api.surus.dev/functions/v1/detokenize"
    data = {
        "tokenizer": "Qwen/Qwen3-1.7B",
        "tokens": [15496, 11, 703, 546, 30]
    }
    response = requests.post(API_URL, json=data)
    print(response.json())
    ```

=== "cURL"
    ```bash
    curl -X POST https://api.surus.dev/functions/v1/detokenize \
      -H "Content-Type: application/json" \
      -d '{"tokenizer": "Qwen/Qwen3-1.7B", "tokens": [15496, 11, 703, 546, 30]}'
    ```

### Respuesta

```json
{
  "text": "Hola, cómo estás?"
}
```

---

## Parámetros

- `tokenizer` (`string`, requerido): Nombre del modelo/tokenizer compatible con HuggingFace.
- `text` (`string`, requerido para tokenización): Texto a tokenizar.
- `tokens` (`list[int]`, requerido para detokenización): Lista de IDs de tokens a convertir en texto.

---

## Notas

- Compatible con cualquier modelo/tokenizer de HuggingFace que soporte la clase `transformers.Tokenizer`.
- Útil para contar tokens, preprocesar datos antes de enviar a modelos, y reconstruir texto desde tokens.