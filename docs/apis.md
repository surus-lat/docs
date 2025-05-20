# APIs y Ejemplos de Uso

En esta sección encontrarás la documentación detallada de cada endpoint disponible en la API de GradienteSur, junto con ejemplos de uso para cada uno.

### Chat Completions
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
    
### Audio Transcriptions
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

### Audio Speech
=== "Python"
    ```python
    import requests

    GS_API_KEY = "tu_clave_api"
    API_URL = "https://api.gradientesur.com/functions/v1/audio/speech"
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
    const API_URL = 'https://api.gradientesur.com/functions/v1/audio/speech';
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
    curl -X POST https://api.gradientesur.com/functions/v1/audio/speech \
      -H "Authorization: Bearer tu_clave_api" \
      -H "Content-Type: application/json" \
      -d '{"model": "marianbasti/Llama-3.2-3B-Orpheus-Rioplatense-1795", "input": "Hola, ¿cómo estás?", "voice": "female", "response_format": "wav"}' --output output.wav
    ```

### Chat Completions con Imagen
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
### Embeddings
=== "Python"
    ```python
    import requests

    GS_API_KEY = "tu_clave_api"
    API_URL = "https://api.gradientesur.com/functions/v1/embeddings"
    headers = {"Authorization": "Bearer " + GS_API_KEY}

    data = {
        "model": "nomic-ai/nomic-embed-text-v1.5",
        "input": ["Hola mundo", "Cómo estás?"]
    }

    response = requests.post(API_URL, headers=headers, json=data)
    print(response.json())
    ```

=== "JavaScript"
    ```javascript
    const GS_API_KEY = "tu_clave_api";
    const API_URL = 'https://api.gradientesur.com/functions/v1/embeddings';
    fetch(API_URL, {
      method: 'POST',
      headers: {
        'Authorization': 'Bearer ' + GS_API_KEY,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        model: 'nomic-ai/nomic-embed-text-v1.5',
        input: ['Hola mundo', 'Cómo estás?']
      })
    })
    .then(res => res.json())
    .then(data => console.log(data));
    ```

=== "cURL"
    ```bash
    curl -X POST https://api.gradientesur.com/functions/v1/embeddings \
      -H "Authorization: Bearer tu_clave_api" \
      -H "Content-Type: application/json" \
      -d '{"model": "nomic-ai/nomic-embed-text-v1.5", "input": ["Hola mundo", "Cómo estás?"]}'
    ```

### Models
```bash
curl -X GET https://api.gradientesur.com/functions/v1/models \
  -H "Authorization: Bearer tu_clave_api"
```

---
