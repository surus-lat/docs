# surus API Docs

Documentación oficial de la API de surus.

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

Porfa revisar `doc_guidelines.md` para ver doc guidelines