"""Extract form field information from PDFs."""
import pdfplumber


def get_form_fields(pdf_path: str) -> list:
    """Return a list of form field names and types."""
    fields = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            if page.annots:
                for annot in page.annots:
                    fields.append({"name": annot.get("T"), "type": annot.get("FT")})
    return fields
