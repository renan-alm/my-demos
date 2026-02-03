"""Create validation images with bounding box overlays."""
from PIL import Image, ImageDraw


def draw_boxes(image_path: str, boxes: list, output_path: str) -> None:
    """Draw bounding boxes on an image for validation."""
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    for box in boxes:
        draw.rectangle(box, outline="red", width=2)
    img.save(output_path)
