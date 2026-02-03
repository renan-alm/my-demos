---
name: pdf-extractor
description: Guide for extracting text and tables from PDF documents using Python. Use this when asked to parse PDFs, extract tables, or read text content from PDF files.
---
# PDF Data Extraction

Use `pdfplumber` for extracting text and tables from PDF documents.

## Extract Text

```python
import pdfplumber

with pdfplumber.open("document.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        print(text)
```

## Extract Tables

```python
with pdfplumber.open("document.pdf") as pdf:
    for i, page in enumerate(pdf.pages):
        tables = page.extract_tables()
        for j, table in enumerate(tables):
            print(f"Table {j+1} on page {i+1}:")
            for row in table:
                print(row)
```

## Advanced Table Extraction

```python
import pandas as pd

with pdfplumber.open("document.pdf") as pdf:
    all_tables = []
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            df = pd.DataFrame(table[1:], columns=table[0])
            all_tables.append(df)
```

## Installation

```bash
pip install pdfplumber pandas
```
