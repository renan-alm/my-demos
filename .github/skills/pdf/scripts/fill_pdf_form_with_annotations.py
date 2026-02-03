"""Fill PDF forms using annotation-based approach."""
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject


def fill_with_annotations(pdf_path: str, data: dict, output_path: str) -> None:
    """Fill form using annotation objects for complex forms."""
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    writer.append(reader)

    for page in writer.pages:
        if "/Annots" in page:
            for annot in page["/Annots"]:
                obj = annot.get_object()
                if obj.get("/T") in data:
                    obj.update({NameObject("/V"): data[obj.get("/T")]})

    with open(output_path, "wb") as f:
        writer.write(f)
