import pandas as pd
import pdfplumber
import re
from datetime import datetime

class ICICIParser:
    def parse(self, pdf_path: str) -> pd.DataFrame:
        try:
            with pdfplumber.open(pdf_path) as pdf:
                text = ""
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
            
            # Process extracted text to create DataFrame
            data = []
            lines = text.split('\n')
            
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                
                # Extract transaction data using regex
                date_match = re.search(r'(\d{2}[/-]\d{2}[/-]\d{4})', line)
                if date_match:
                    amounts = re.findall(r'([\d,]+\.\d{2})', line)
                    if amounts:
                        data.append({
                            'date': date_match.group(1),
                            'description': 'Transaction',
                            'debit': amounts[0] if len(amounts) > 0 else '',
                            'credit': '',
                            'balance': amounts[-1] if amounts else ''
                        })
            
            return pd.DataFrame(data)
            
        except Exception as e:
            print(f"Parse error: {e}")
            return pd.DataFrame(columns=['date', 'description', 'debit', 'credit', 'balance'])