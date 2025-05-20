# Inicio rápido


Este es un ejemplo básico de cómo realizar una llamada a la API de chat:

=== "Python"
    ```python
    import requests

    GS_API_KEY = "tu_clave_api"
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