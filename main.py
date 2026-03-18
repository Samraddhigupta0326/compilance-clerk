import os
import pandas as pd
from parser import extract_text
from llm_handler import extract_with_llm
from logger import log_llm

# create folders if not exist
os.makedirs("logs", exist_ok=True)
os.makedirs("output", exist_ok=True)

# path to pdf
pdf_path = "sample_pdfs/sample1.pdf"

# extract text
text = extract_text(pdf_path)

# extract structured data
data = extract_with_llm(text)

print("Extracted Data:")
print(data)

# logging (audit trail)
print("Logging now...")
log_llm(text, data)

# save to CSV
df = pd.DataFrame([data])
df.to_csv("output/data.csv", mode="a", header=not os.path.exists("output/data.csv"), index=False)