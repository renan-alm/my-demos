"""Check for fillable form fields in a PDF."""
import pdfplumber


def has_fillable_fields(pdf_path: str) -> bool:
    """Return True if the PDF contains fillable form fields."""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            if page.annots:
                return True
    return False
