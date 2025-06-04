# Audio Speech

Este endpoint convierte texto en audio hablado. Lo podés usar en aplicaciones que necesiten generar audio a partir de texto, como asistentes virtuales, audiolibros, etc.

### Solicitud

=== "Python"
    ```python
    import requests

    GS_API_KEY = "tu_clave_api"
    API_URL = "https://api.surus.dev/functions/v1/audio/speech"
    headers = {"Authorization": "Bearer " + GS_API_KEY}

    data = {
        "model": "marianbasti/Llama-3.2-3B-Orpheus-Rioplatense-1795",
        "input": "Hola, ¿cómo estás?",
        "voice": "female",
        "response_format": "wav"
    }

    response = requests.post(API_URL, headers=headers, json=data)
    with open("output.wav", "wb") as f:
        f.write(response.content)
    ```

=== "JavaScript"
    ```javascript
    const GS_API_KEY = "tu_clave_api";
    const API_URL = 'https://api.surus.dev/functions/v1/audio/speech';
    fetch(API_URL, {
      method: 'POST',
      headers: {
        'Authorization': 'Bearer ' + GS_API_KEY,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        model: 'marianbasti/Llama-3.2-3B-Orpheus-Rioplatense-1795',
        input: 'Hola, ¿cómo estás?',
        voice: 'female',
        response_format: 'wav'
      })
    })
    .then(res => res.blob())
    .then(blob => {
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'output.wav';
      a.click();
    });
    ```

=== "cURL"
    ```bash
    curl -X POST https://api.surus.dev/functions/v1/audio/speech \
      -H "Authorization: Bearer tu_clave_api" \
      -H "Content-Type: application/json" \
      -d '{"model": "marianbasti/Llama-3.2-3B-Orpheus-Rioplatense-1795", "input": "Hola, ¿cómo estás?", "voice": "female", "response_format": "wav"}' --output output.wav
    ```

### Respuesta

```json
{
    "audio": "data:audio/wav;base64,UklGRiQAAABXQVZFZm10IBAAAAABAAEAgD4AAAB9AAACABAAZGF0YQ=="
}
```
El audio generado se devuelve en formato WAV. En el ejemplo de Python y cURL, se guarda directamente en un archivo llamado `output.wav`. En JavaScript, se crea un enlace para descargar el archivo generado.---
