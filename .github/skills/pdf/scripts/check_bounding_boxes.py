"""Extract bounding boxes from PDF elements."""
import pdfplumber


def get_bounding_boxes(pdf_path: str) -> list:
    """Return bounding boxes for all elements in the PDF."""
    boxes = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            for char in page.chars:
                boxes.append(char["bbox"])
    return boxes
