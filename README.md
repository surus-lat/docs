# Actualización automática de modelos y precios

Los archivos `modelos.md` y `pricings.md` se generan automáticamente desde la API de GradienteSur cada vez que se construye la documentación.

Para actualizar manualmente:

```bash
export GRADIENTESUR_API_KEY="<tu_api_key>"
python scripts/gen_models_and_pricing.py
```

En ReadTheDocs, agrega este script como un paso previo a la construcción en tu configuración (`.readthedocs.yaml`):

```yaml
build:
  jobs:
    pre_build:
      - export GRADIENTESUR_API_KEY=... # o usa un secreto
      - python scripts/gen_models_and_pricing.py
```
# GradienteSur API Docs

Documentación oficial de la API de GradienteSur.

## Estructura

La documentación está en la carpeta `docs/` y sigue el formato de [MkDocs](https://www.mkdocs.org/) para ser publicada en ReadTheDocs o cualquier hosting estático.

## Cómo construir la documentación localmente

1. Instalá los requerimientos:
   ```bash
   pip install -r requirements.txt
   ```
2. Levantá un servidor local para previsualizar:
   ```bash
   mkdocs serve
   ```
3. Abrí tu navegador en http://localhost:8000

---

## Estructura de la documentación

- `docs/index.md`: Introducción general
- `docs/comenzando/autenticacion.md`: Cómo autenticarse
- `docs/comenzando/index.md`: Inicio rápido
- `docs/apis.md`: APIs y ejemplos de uso
- `docs/modelos.md`: Modelos disponibles
- `docs/pricings.md`: Precios
- `mkdocs.yml`: Configuración de la documentación y navegación
- `scripts/gen_index.py`: Script para generar el índice dinámico

---

## Generación automática del índice

El archivo `docs/index.md` se genera automáticamente a partir de la estructura definida en `mkdocs.yml` usando el script `scripts/gen_index.py` y el plugin `mkdocs-gen-files`. No edites `index.md` manualmente.

Para regenerar el índice:

```bash
python scripts/gen_index.py
```

O simplemente al correr `mkdocs serve` o `mkdocs build`, el índice se actualizará automáticamente.

---

## Contribuciones

¡Te invitamos a contribuir a la documentación! Si quisieras hacerlo, crea un issue o pull request.