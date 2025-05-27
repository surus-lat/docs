# Audio Transcriptions

Este endpoint convierte archivos de audio en texto. Es útil para transcribir grabaciones, entrevistas, etc.

=== "Python"
    ```python
    import requests

    GS_API_KEY = "tu_clave_api"
    API_URL = "https://api.gradientesur.com/functions/v1/audio/transcriptions"
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
    const API_URL = 'https://api.gradientesur.com/functions/v1/audio/transcriptions';
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
    curl -X POST https://api.gradientesur.com/functions/v1/audio/transcriptions \
      -H "Authorization: Bearer tu_clave_api" \
      -F "model=marianbasti/whisper-large-v3-turbo-latam" \
      -F "audio=@file.wav"
    ```
    
## Ejemplo de respuesta:
```json
{
  "text": "Hola, ¿cómo estás?"
}
```
---
