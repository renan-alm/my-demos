# PDF Forms Reference

## Supported Form Types

- **AcroForms**: Standard PDF forms with fillable fields
- **XFA Forms**: XML-based forms (limited support)

## Common Field Types

| Type | Code | Description |
|------|------|-------------|
| Text | `/Tx` | Single or multi-line text input |
| Button | `/Btn` | Checkboxes, radio buttons, push buttons |
| Choice | `/Ch` | Dropdowns and list boxes |
| Signature | `/Sig` | Digital signature fields |

## Example: Detecting Form Type

```python
from pypdf import PdfReader

reader = PdfReader("form.pdf")
if "/AcroForm" in reader.trailer["/Root"]:
    print("Contains AcroForm fields")
```
