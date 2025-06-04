# Audio Transcriptions

Este endpoint convierte archivos de audio en texto. Es útil para transcribir grabaciones, entrevistas, etc.

## Solicitud

=== "Python"
    ```python
    import requests

    GS_API_KEY = "tu_clave_api"
    API_URL = "https://api.surus.dev/functions/v1/audio/transcriptions"
    headers = {"Authorization": "Bearer " + GS_API_KEY}

    with open('audio.wav', 'rb') as f:
        files = {'audio': f}
        data = {'model': 'marianbasti/whisper-large-v3-turbo-latam'}
        response = requests.post(API_URL, headers=headers, data=data, files=files)
        print(response.json())
    ```

=== "JavaScript"
    ```javascript
    const GS_API_KEY = "tu_clave_api";
    const API_URL = 'https://api.surus.dev/functions/v1/audio/transcriptions';
    const formData = new FormData();
    formData.append('model', 'marianbasti/whisper-large-v3-turbo-latam');
    formData.append('audio', audioFileInput.files[0]); // audioFileInput is an <input type='file'>
    fetch(API_URL, {
      method: 'POST',
      headers: {
        'Authorization': 'Bearer ' + GS_API_KEY
      },
      body: formData
    })
    .then(res => res.json())
    .then(data => console.log(data));
    ```

=== "cURL"
    ```bash
    curl -X POST https://api.surus.dev/functions/v1/audio/transcriptions \
      -H "Authorization: Bearer tu_clave_api" \
      -F "model=marianbasti/whisper-large-v3-turbo-latam" \
      -F "audio=@file.wav"
    ```
    
### Respuesta

```json
{
  "text": "Hola, ¿cómo estás?"
}
```

---

## Parámetros extra

Podés enviar los siguientes parámetros adicionales para controlar el comportamiento de la generación y el formato de la respuesta.

### Parámetros de formato y salida

- `response_format` (`string`, default: `"json"`): El formato de la salida. Opciones: `json`, `text`, `srt`, `verbose_json`, o `vtt`. Para algunos modelos, solo se soporta `json`.
- `stream` (`bool`, default: `False`): Si se establece en `true`, la respuesta será transmitida al cliente usando server-sent events. Nota: No todos los modelos soportan streaming.
- `temperature` (`number`, default: `0`): La temperatura de muestreo, entre 0 y 1. Valores más altos como 0.8 harán la salida más aleatoria, mientras que valores más bajos como 0.2 la harán más enfocada y determinística.
- `timestamp_granularities` (`array`, default: `["segment"]`): La granularidad de timestamps a incluir. Debe usarse con `response_format` establecido en `verbose_json`. Opciones: `word`, `segment`.

=== "Python"
    ```python
    import requests

    GS_API_KEY = "tu_clave_api"
    API_URL = "https://api.surus.dev/functions/v1/audio/transcriptions"
    headers = {"Authorization": "Bearer " + GS_API_KEY}

    with open('audio.wav', 'rb') as f:
        files = {'audio': f}
        data = {
            'model': 'marianbasti/whisper-large-v3-turbo-latam',
            'response_format': 'verbose_json',
            'temperature': 0.2,
            'timestamp_granularities': ['word', 'segment']
        }
        response = requests.post(API_URL, headers=headers, data=data, files=files)
        print(response.json())
    ```

=== "JavaScript"
    ```javascript
    const GS_API_KEY = "tu_clave_api";
    const API_URL = 'https://api.surus.dev/functions/v1/audio/transcriptions';
    const formData = new FormData();
    formData.append('model', 'marianbasti/whisper-large-v3-turbo-latam');
    formData.append('audio', audioFileInput.files[0]);
    formData.append('response_format', 'verbose_json');
    formData.append('temperature', '0.2');
    formData.append('timestamp_granularities', 'word');
    formData.append('timestamp_granularities', 'segment');
    
    fetch(API_URL, {
      method: 'POST',
      headers: {
        'Authorization': 'Bearer ' + GS_API_KEY
      },
      body: formData
    })
    .then(res => res.json())
    .then(data => console.log(data));
    ```

=== "cURL"
    ```bash
    curl -X POST https://api.surus.dev/functions/v1/audio/transcriptions \
      -H "Authorization: Bearer tu_clave_api" \
      -F "model=marianbasti/whisper-large-v3-turbo-latam" \
      -F "audio=@file.wav" \
      -F "response_format=verbose_json" \
      -F "temperature=0.2" \
      -F "timestamp_granularities=word" \
      -F "timestamp_granularities=segment"
    ```

---
