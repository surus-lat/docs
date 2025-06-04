# Embeddings

Este endpoint genera representaciones vectoriales (embeddings) de texto. Los embeddings son útiles para crear bases de datos vectoriales para tareas como búsqueda semántica, clustering y clasificación de texto.

### Solicitud

=== "Python"
    ```python
    import requests

    SURUS_API_KEY = "tu_clave_api"
    API_URL = "https://api.surus.dev/functions/v1/embeddings"
    headers = {"Authorization": "Bearer " + SURUS_API_KEY}

    data = {
        "model": "nomic-ai/nomic-embed-text-v1.5",
        "input": ["Hola mundo", "Cómo estás?"]
    }

    response = requests.post(API_URL, headers=headers, json=data)
    print(response.json())
    ```

=== "JavaScript"
    ```javascript
    const SURUS_API_KEY = "tu_clave_api";
    const API_URL = 'https://api.surus.dev/functions/v1/embeddings';
    fetch(API_URL, {
      method: 'POST',
      headers: {
        'Authorization': 'Bearer ' + SURUS_API_KEY,
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
    curl -X POST https://api.surus.dev/functions/v1/embeddings \
      -H "Authorization: Bearer tu_clave_api" \
      -H "Content-Type: application/json" \
      -d '{"model": "nomic-ai/nomic-embed-text-v1.5", "input": ["Hola mundo", "Cómo estás?"]}'
    ```
    
### Respuesta:

```json
{
    "object": "list",
    "data": [
    {
        "object": "embedding",
        "embedding": [0.012, -0.034, 0.567, ...],
        "index": 0
    },
    {
        "object": "embedding",
        "embedding": [0.045, -0.021, 0.432, ...],
      "index": 1
    }
    ],
    "model": "nomic-ai/nomic-embed-text-v1.5",
    "usage": {
        "prompt_tokens": 21,
        "total_tokens": 21
    },
    "id": "infinity-1d83ebb5-4546-4a2e-b15e-a546e399d5d1",
    "created": 1748351941
}
```

## Cantidad de dimensiones
En el caso que que querramos una dimensionalidad más comprimida (en vez de las 768 dimensiones por defecto), podemos especificar el parámetro `dimensions` en la petición. Por ejemplo, para obtener embeddings de 256 dimensiones:

=== "Python"
    ```python
    import requests

    SURUS_API_KEY = "tu_clave_api"
    API_URL = "https://api.surus.dev/functions/v1/embeddings"
    headers = {"Authorization": "Bearer " + SURUS_API_KEY}

    data = {
        "model": "nomic-ai/nomic-embed-text-v1.5",
        "input": ["Hola mundo", "Cómo estás?"],
        "dimensions": 256
    }

    response = requests.post(API_URL, headers=headers, json=data)
    print(response.json())
    ```

=== "JavaScript"
    ```javascript
    const SURUS_API_KEY = "tu_clave_api";
    const API_URL = 'https://api.surus.dev/functions/v1/embeddings';
    fetch(API_URL, {
      method: 'POST',
      headers: {
        'Authorization': 'Bearer ' + SURUS_API_KEY,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
          model: 'nomic-ai/nomic-embed-text-v1.5',
          input: ['Hola mundo', 'Cómo estás?'],
          dimensions: 256
        })
    })
    .then(res => res.json())
    .then(data => console.log(data));
    ```

=== "cURL"
    ```bash
    curl -X POST https://api.surus.dev/functions/v1/embeddings \
      -H "Authorization: Bearer tu_clave_api" \
      -H "Content-Type: application/json" \
      -d '{"model": "nomic-ai/nomic-embed-text-v1.5", "input": ["Hola mundo", "Cómo estás?"], "dimensions": 256}'
    ```

---