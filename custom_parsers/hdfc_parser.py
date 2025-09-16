import pandas as pd
import pdfplumber
import re
from datetime import datetime

class HDFCParser:
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
                
                # Extract transaction data using regex for the ICICI format
                # Look for date pattern DD/MM/YYYY
                date_match = re.search(r'(\d{2}/\d{2}/\d{4})', line)
                if date_match:
                    date_str = date_match.group(1)
                    
                    # Convert date to YYYY-MM-DD format
                    try:
                        date_obj = datetime.strptime(date_str, '%d/%m/%Y')
                        formatted_date = date_obj.strftime('%Y-%m-%d')
                    except:
                        formatted_date = date_str
                    
                    # Extract description (text after date, before amounts)
                    remaining_line = line[line.find(date_str) + len(date_str):].strip()
                    
                    # Find all amounts in the line
                    amounts = re.findall(r'(\d+\.?\d*)', remaining_line)
                    
                    if amounts:
                        # Parse the line structure: DATE DESCRIPTION DEBIT CREDIT BALANCE
                        parts = remaining_line.split()
                        
                        # Extract description (everything before the amounts)
                        desc_parts = []
                        amount_found = False
                        for part in parts:
                            if re.match(r'\d+\.?\d*', part):
                                amount_found = True
                                break
                            desc_parts.append(part)
                        
                        description = ' '.join(desc_parts) if desc_parts else 'Transaction'
                        
                        # Determine debit/credit based on position and keywords
                        debit = ''
                        credit = ''
                        balance = amounts[-1] if amounts else ''
                        
                        # Simple logic: if description contains credit keywords, it's credit
                        if any(word in description.lower() for word in ['credit', 'salary', 'interest', 'dividend']):
                            if len(amounts) >= 2:
                                credit = amounts[-2]
                        else:
                            # It's likely a debit
                            if len(amounts) >= 2:
                                debit = amounts[-2]
                        
                        data.append({
                            'date': formatted_date,
                            'description': description[:50],  # Limit description length
                            'debit': debit,
                            'credit': credit,
                            'balance': balance
                        })
            
            return pd.DataFrame(data)
            
        except Exception as e:
            print(f"Parse error: {e}")
            return pd.DataFrame(columns=['date', 'description', 'debit', 'credit', 'balance'])