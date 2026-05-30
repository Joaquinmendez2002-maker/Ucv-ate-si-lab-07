from kedro.pipeline import Pipeline, node, pipeline
from .nodes import process_image  # 👈 Asegúrate de que tenga el puntito adelante

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=process_image,
                inputs="raw_image",
                outputs="processed_image",
                name="process_image_node",
            ),
        ]
    )