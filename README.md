# si-image-processing-lab

Resumen profesional
-------------------

Laboratorio de procesamiento de imágenes desarrollado como proyecto académico/profesional. Este repositorio contiene una pequeña aplicación basada en Kedro para demostrar un pipeline de ingestión y procesamiento de imágenes (rotación, filtros y anotación), empaquetada como `si_image_processing_lab`.

Características principales
- Pipeline de procesamiento de imágenes con Kedro.
- Transformaciones de imagen usando Pillow (rotación, filtros, anotado de texto).
- Estructura de proyecto preparada para Poetry y pruebas con `pytest`.

Estado del proyecto
- Versión: 0.1.0
- Lenguaje: Python 3.10+
- Herramientas: Kedro, Poetry

Requisitos
- Python 3.10 - 3.14
- Ver [si-image-processing-lab/pyproject.toml](si-image-processing-lab/pyproject.toml) y [si-image-processing-lab/requirements.txt](si-image-processing-lab/requirements.txt) para dependencias detalladas.

Instalación rápida
1. Clonar el repositorio:

```bash
git clone <repo-url>
cd Ucv-ate-si-lab-07/si-image-processing-lab
```

2. (Recomendado) Crear un entorno virtual y activar:

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows: .venv\Scripts\activate
```

3. Instalar dependencias:

Con Poetry:

```bash
poetry install
```

Con pip (si no usa Poetry):

```bash
pip install -r requirements.txt
```

Uso
- Ejecutar el pipeline con Kedro (desde la carpeta `si-image-processing-lab`):

```bash
kedro run
```

- También es posible ejecutar el paquete como módulo Python:

```bash
python -m si_image_processing_lab
```

Estructura del proyecto (resumen)
- `si-image-processing-lab/` — proyecto principal gestionado con Poetry.
- `si-image-processing-lab/src/si_image_processing_lab/` — paquete Python principal.
	- `pipeline_registry.py` — registro de pipelines del proyecto.
	- `settings.py` — configuración del proyecto Kedro.
	- `pipelines/image_processing/` — pipeline y nodos de procesamiento de imagen (`pipeline.py`, `nodes.py`).
- `conf/` — configuraciones por ambiente (base, local).
- `data/` — directorios de datos (raw, primary, ...).

Descripción técnica breve
- El pipeline principal está definido en `src/si_image_processing_lab/pipelines/image_processing/pipeline.py` y contiene un único nodo `process_image` (implementado en `nodes.py`) que aplica transformaciones usando Pillow.
- El registro de pipelines se expone en `src/si_image_processing_lab/pipeline_registry.py`.

Buenas prácticas y recomendaciones
- Añadir ejemplos de entrada/salida en `data/03_primary` para facilitar pruebas reproducibles.
- Documentar parámetros configurables en `conf/base/parameters.yml` si se agregan más transformaciones.
- Añadir un script de ejemplo en `notebooks/` que muestre el flujo de datos y salida visual.

Contribuciones
- Fork + pull request. Abrir un issue antes de cambios grandes para discutir la implementación.

Licencia
- Indique aquí la licencia del proyecto (p. ej. MIT) o borre esta sección si no aplica.

Contacto
- Equipo / Autor: UCV - Ingeniería de Sistemas

Notas finales
- Si desea, puedo:
	- añadir ejemplos concretos de uso (comandos y sample images),
	- completar la sección de licencia,
	- generar un `CONTRIBUTING.md` y plantillas de GitHub Actions para CI.
