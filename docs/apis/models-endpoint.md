# Modelos

Con este endpoint obtenés una lista de todos los modelos de IA actualmente disponibles a través de la API de surus.

La página general de [Modelos Disponibles](../modelos.md) se actualiza dinámicamente usando este endpoint.

### Solicitud
```bash
curl -X GET https://api.surus.dev/functions/v1/models \
  -H "Authorization: Bearer tu_clave_api"
```

### Respuesta
```json
{
  "data": [
    {
      "name": "marianbasti/Llama-3.2-3B-Orpheus-Rioplatense-1795",
      "type": "audio",
      "task": "text_to_speech",
      "documentation_url": "https://huggingface.co/marianbasti/Llama-3.2-3B-Orpheus-Rioplatense-1795",
      "description": "Nuestro modelo propietario de texto a voz entrenado para el español rioplatense.",
      "unique_selling_point": "Texto a voz | Español Rioplatense",
      "use_cases": [
        "Asistente de voz",
        "Audiolibros",
        "Accessibilidad",
        "Aprender Español"
      ],
      "specifications": {
        "Idiomas": "es-AR",
        "Licencia": "llama3.2",
        "Parametros": "3B",
        "Arquitectura": "Orpheus-TTS",
        "Longitud de contexto": 4096
      },
      "pricing": {
        "input": "0.00000000",
        "output": "0.00022500",
        "unit": "seconds"
      },
      "object": "model",
      "owned_by": "SURUS",
      "created": "2025-05-12T16:43:50.016525+00:00"
    },
    {
      "name": "Qwen/Qwen3-1.7B",
      "type": "text",
      "task": "text_generation",
      "documentation_url": "https://huggingface.co/Qwen/Qwen3-1.7B",
      "description": "Modelo pequeño entrenado para razonamiento, con la capacidad de realizar tareas simples de manera rápida.",
      "unique_selling_point": "Razonador | Pequeño y rápido",
      "use_cases": [
        "Chatbots",
        "Generación de contenido",
        "Resúmenes",
        "Razonamiento"
      ],
      "specifications": {
        "Idiomas": "en",
        "Licencia": "MIT",
        "Parametros": "1.7B",
        "Arquitectura": "Transformer",
        "Longitud de contexto": 24000
      },
      "pricing": {
        "input": "0.09000000",
        "output": "0.36000000",
        "unit": "1M tokens"
      },
      "object": "model",
      "owned_by": "SURUS",
      "created": "2025-05-12T22:16:39.169061+00:00"
    }
    // Otros modelos...
  ]
}
```
---
