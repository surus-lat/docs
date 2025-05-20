# GradienteSur API Docs

Documentación oficial de la API de GradienteSur, compatible con OpenAI.

## Estructura

La documentación está en la carpeta `docs/` y sigue el formato de [MkDocs](https://www.mkdocs.org/) para ser publicada en ReadTheDocs.

## Cómo construir la documentación localmente

1. Instala MkDocs y el tema Material:
   ```bash
   pip install mkdocs mkdocs-material
   ```
2. Levanta un servidor local para previsualizar:
   ```bash
   mkdocs serve
   ```
3. Abre tu navegador en http://localhost:8000

## Publicación en ReadTheDocs

- Vincula este repositorio en https://readthedocs.org/
- ReadTheDocs detectará automáticamente el archivo `mkdocs.yml` y construirá la documentación.

---

## Estructura de la documentación

- `docs/index.md`: Introducción general
- `docs/autenticacion.md`: Cómo autenticarse
- `docs/endpoints.md`: Descripción de los endpoints
- `docs/ejemplos.md`: Ejemplos de uso
- `docs/faq.md`: Preguntas frecuentes
- `mkdocs.yml`: Configuración de la documentación
