"""Fill PDF form fields programmatically."""
from pypdf import PdfReader, PdfWriter


def fill_form(pdf_path: str, data: dict, output_path: str) -> None:
    """Fill form fields with provided data and save to output."""
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    writer.append(reader)
    writer.update_page_form_field_values(writer.pages[0], data)
    with open(output_path, "wb") as f:
        writer.write(f)
