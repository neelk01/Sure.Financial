# SURE - PDF Statement Parser

SURE is a Python project to extract key information from bank statement PDFs and save it into a CSV file for easy analysis.

## Project Structure

SURE/
- parse_statements.py       # Script to parse PDFs
- pdfs/                     # Folder containing PDF statements
  - axis_statement.pdf
  - hdfc_statement.pdf
  - icici_statement.pdf
  - kotak_statement.pdf
  - sbi_statement.pdf
- parsed_output.csv         # CSV output generated after running the script

## Features

- Extracts from each PDF:
  - Name
  - Last 4 digits of Card Number
  - Statement Period
  - Total Amount Due
  - Payment Due Date
- Automatically detects bank name from PDF filename
- Fields not found are marked as `Not Found`

## Requirements

- Python 3.7 or higher
- Libraries: `pdfplumber`, `pandas`
