# Autenticación

Para utilizar la API de GradienteSur es necesario autenticarse mediante una API Key.

Es una clave única que te identifica como usuario y te permite acceder a los servicios de la API de GradienteSur. Es importante mantenerla segura y no compartirla públicamente.

## ¿Cómo obtengo mi API Key?

Podés generar tu API Key accediendo a [https://surus.dev/api-keys](https://surus.dev/api-keys). Si tienes problemas para obtenerla, contacta a soporte.

## ¿Cómo se usa la API Key?


Debes incluir la API Key en el encabezado `Authorization` de cada petición, precedida por la palabra `Bearer`. Por ejemplo:

=== "Python"
    ```python
    import requests
    url = "https://api.surus.dev/functions/v1/models"
    headers = {"Authorization": "Bearer tu_clave_api"}
    response = requests.get(url, headers=headers)
    print(response.json())
    ```

=== "JavaScript"
    ```js
    const fetch = require('node-fetch');
    const url = 'https://api.surus.dev/functions/v1/models';
    const headers = {
      'Authorization': 'Bearer tu_clave_api'
    };
    fetch(url, {
      method: 'GET',
      headers: headers
    })
      .then(res => res.json())
      .then(json => console.log(json));
    ```

=== "cURL"
    ```bash
    curl -X GET https://api.surus.dev/functions/v1/models \
      -H "Authorization: Bearer tu_clave_api"
    ```

En los ejemplos de uso de la documentación, reemplaza `tu_clave_api` por tu clave personal.

---
