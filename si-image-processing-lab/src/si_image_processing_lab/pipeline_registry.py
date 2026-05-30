from typing import Dict
from kedro.pipeline import Pipeline
# Importamos directamente la función creadora desde el archivo pipeline
from si_image_processing_lab.pipelines.image_processing.pipeline import create_pipeline

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines."""
    # Instanciamos manualmente tu pipeline de procesamiento de imágenes
    image_processing_pipeline = create_pipeline()
    
    return {
        "__default__": image_processing_pipeline,
        "image_processing": image_processing_pipeline,
    }