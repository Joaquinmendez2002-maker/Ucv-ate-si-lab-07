from PIL import Image, ImageFilter, ImageDraw

def process_image(image: Image.Image) -> Image.Image:
    """
    Recibe una imagen desde el catálogo, la procesa y la devuelve.
    """
    # 1. Rotar la imagen 45 grados
    rotated = image.rotate(45)
    
    # 2. Aplicar el filtro de relieve
    filtered = rotated.filter(ImageFilter.EMBOSS)
    
    # 3. Dibujar el texto
    draw = ImageDraw.Draw(filtered)
    draw.text((20, 20), "UCV - Sistemas Inteligentes", fill="white")
    
    # 4. Retornar el objeto transformado
    return filtered