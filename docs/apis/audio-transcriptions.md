# Audio Transcriptions

Convierte archivos de audio en texto y texto en audio.

## Transcriptions

Convierte archivos de audio en texto.

### Quick Start

=== "Python"
    ```python
    import requests

    SURUS_API_KEY = "tu_clave_api"
    API_URL = "https://api.surus.dev/functions/v1/audio/transcriptions"
    headers = {"Authorization": "Bearer " + SURUS_API_KEY}

    with open('audio.wav', 'rb') as f:
        files = {'file': f}
        data = {'model': 'nvidia/canary-1b-v2'}
        response = requests.post(API_URL, headers=headers, data=data, files=files)
        print(response.json())
    ```

=== "JavaScript"
    ```javascript
    const form = new FormData();
    form.append('file', fileInput.files[0]);
    form.append('model', 'nvidia/canary-1b-v2');
    fetch('https://api.surus.dev/functions/v1/audio/transcriptions', { 
      method: 'POST', 
      headers: { 'Authorization': 'Bearer tu_clave_api' }, 
      body: form 
    }).then(r=>r.json()).then(console.log);
    ```

### Parámetros

- `model`: `nvidia/canary-1b-v2`
- `file`: Archivo de audio a transcribir
- `source_lang` (opcional): Idioma del audio (ej: `es`, `en`, `fr`)
- `target_lang` (opcional): Idioma de la transcripción (ej: `es`, `en`, `fr`)

### Respuesta

```json
{
  "text": "Hola, ¿cómo estás?"
}
```

### Traducción

Transcribir audio en un idioma y obtener texto en otro:

=== "Python"
    ```python
    import requests

    SURUS_API_KEY = "tu_clave_api"
    headers = {"Authorization": "Bearer " + SURUS_API_KEY}

    with open('english_audio.wav', 'rb') as f:
        files = {'file': f}
        data = {
            'model': 'nvidia/canary-1b-v2',
            'source_lang': 'en',  # audio en inglés
            'target_lang': 'es'   # transcripción en español
        }
        response = requests.post(
            'https://api.surus.dev/functions/v1/audio/transcriptions',
            headers=headers, data=data, files=files
        )
        print(response.json())
    ```

=== "JavaScript"
    ```javascript
    const form = new FormData();
    form.append('file', englishAudioFile);
    form.append('model', 'nvidia/canary-1b-v2');
    form.append('source_lang', 'en');  // audio en inglés
    form.append('target_lang', 'es');  // transcripción en español
    
    fetch('https://api.surus.dev/functions/v1/audio/transcriptions', {
      method: 'POST',
      headers: { 'Authorization': 'Bearer tu_clave_api' },
      body: form
    }).then(r => r.json()).then(console.log);
    ```

**Idiomas soportados:** `es`, `en`, `fr`, `de`, `it`, `pt`, `ru`, `zh`, `ja`, `ko` y 15 más.

---

## Speech Synthesis

Convierte texto en audio.

### Quick Start

=== "Python"
    ```python
    import requests

    SURUS_API_KEY = "tu_clave_api"
    API_URL = "https://api.surus.dev/functions/v1/audio/speech"
    headers = {"Authorization": "Bearer " + SURUS_API_KEY, "Content-Type": "application/json"}

    data = {
        'model': 'surus-lat/Llama-3.2-3B-Orpheus-Rioplatense-1795',
        'input': 'Hola, ¿cómo estás?',
        'voice': 'female',
        'response_format': 'wav'
    }
    response = requests.post(API_URL, headers=headers, json=data)
    
    with open('output.wav', 'wb') as f:
        f.write(response.content)
    ```

=== "JavaScript"
    ```javascript
    fetch('https://api.surus.dev/functions/v1/audio/speech', {
      method: 'POST',
      headers: {
        'Authorization': 'Bearer tu_clave_api',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        model: 'surus-lat/Llama-3.2-3B-Orpheus-Rioplatense-1795',
        input: 'Hola, ¿cómo estás?',
        voice: 'female',
        response_format: 'wav'
      })
    })
    .then(r => r.blob())
    .then(blob => {
      const url = URL.createObjectURL(blob);
      const audio = new Audio(url);
      audio.play();
    });
    ```

### Parámetros

- `model`: `surus-lat/Llama-3.2-3B-Orpheus-Rioplatense-1795`
- `input`: Texto a convertir en audio
- `voice`: `female` o `male`
- `response_format`: `wav`, `mp3`, etc.

