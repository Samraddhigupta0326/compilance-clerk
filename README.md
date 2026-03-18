# The Compliance Clerk – Intelligent Document Extraction

## Overview

The Compliance Clerk is a backend-focused Python application that automates the extraction of structured data from PDF documents such as eChallan and Non-Agricultural (NA) permission files.

It reads PDFs, extracts text (with OCR fallback), processes the content into structured JSON, and exports the results into a CSV file. The system also maintains audit logs for traceability.

---

## Features

* Multi-format PDF parsing (eChallan & NA documents)
* OCR fallback for image-based PDFs
* Structured data extraction
* CSV export for processed data
* Audit logging using JSONL

---

## Project Structure

```
compliance-clerk/
│
├── main.py
├── parser.py
├── llm_handler.py
├── logger.py
├── sample_pdfs/
├── output/
├── logs/
```

---

## Installation

1. Install Python (3.10+ recommended)

2. Install dependencies:

```
pip install pdfplumber pytesseract pillow pandas python-dotenv flask
```

---

## How to Run

```
python main.py
```

---

## Output

* Extracted data is saved in:

  ```
  output/data.csv
  ```

* Logs are stored in:

  ```
  logs/llm_logs.jsonl
  ```

---

## Notes

* OCR is used when text is not directly extractable from PDFs.
* A rule-based extraction approach is used as a fallback due to API limitations.


