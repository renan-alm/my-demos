"""Convert PDF pages to images."""
from pdf2image import convert_from_path


def pdf_to_images(pdf_path: str, output_dir: str) -> list:
    """Convert each PDF page to a PNG image."""
    images = convert_from_path(pdf_path)
    paths = []
    for i, image in enumerate(images):
        path = f"{output_dir}/page_{i + 1}.png"
        image.save(path, "PNG")
        paths.append(path)
    return paths
