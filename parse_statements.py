import pdfplumber
import re
import pandas as pd
import os

# Folder containing your generated PDFs
PDF_FOLDER = "pdfs"

# Prepare list to store extracted data
records = []

# Regex patterns for each field
patterns = {
    "name": r"Name:\s*(.+)",
    "card_last4": r"Card Number:\s*.*(\d{4})",
    "period": r"Statement Period:\s*(.+)",
    "total_due": r"Total Amount Due:\s*(Rs\.\s*[\d,]+\.\d{2})",
    "due_date": r"Payment Due Date:\s*(\d{2}\s\w{3}\s\d{4})",
}

# Loop through all PDF files
for filename in os.listdir(PDF_FOLDER):
    if not filename.endswith(".pdf"):
        continue

    filepath = os.path.join(PDF_FOLDER, filename)
    data = {"bank": filename.replace("_statement.pdf", "").upper()}

    with pdfplumber.open(filepath) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"

    # Extract using regex
    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        data[key] = match.group(1).strip() if match else "Not Found"

    records.append(data)

# Convert to DataFrame
df = pd.DataFrame(records)

# Save results
output_path = os.path.join(PDF_FOLDER, "parsed_output.csv")
df.to_csv(output_path, index=False, encoding="utf-8")

print("Extraction complete!")
print(f"\nResults saved to: {output_path}")
