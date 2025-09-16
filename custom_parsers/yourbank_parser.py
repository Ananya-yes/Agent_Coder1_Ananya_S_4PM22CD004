import pdfplumber
import pandas as pd
import re
from datetime import datetime

class YOURBANKParser:
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
                
                # Look for transaction lines with format: DD-MM-YYYY UPI:... amount amount
                date_match = re.search(r'(\d{2}-\d{2}-\d{4})\s+(.+)', line)
                if date_match:
                    date_str = date_match.group(1)
                    rest_of_line = date_match.group(2)
                    
                    # Convert date to YYYY-MM-DD format
                    try:
                        date_obj = datetime.strptime(date_str, '%d-%m-%Y')
                        formatted_date = date_obj.strftime('%Y-%m-%d')
                    except:
                        formatted_date = date_str
                    
                    # Extract UPI transaction description
                    if 'UPI:' in rest_of_line:
                        # Find the UPI part
                        upi_start = rest_of_line.find('UPI:')
                        upi_part = rest_of_line[upi_start:]
                        
                        # Extract description (everything before the amounts at the end)
                        # Look for amounts pattern at the end: space + number + space + number
                        amounts_match = re.search(r'\s+([\d,]+\.\d{2})\s+([\d,]+\.\d{2})\s*$', upi_part)
                        
                        if amounts_match:
                            # Extract description (everything before the amounts)
                            desc_end = upi_part.rfind(amounts_match.group(0))
                            description = upi_part[:desc_end].strip()[:80]  # Limit length
                            
                            # Extract amounts
                            amount1 = amounts_match.group(1).replace(',', '')
                            amount2 = amounts_match.group(2).replace(',', '')
                            
                            # Determine which is debit/credit and which is balance
                            # Usually: [transaction_amount] [balance]
                            # If balance > transaction amount, it's likely credit
                            # If balance < previous balance, it's likely debit
                            
                            balance = amount2
                            transaction_amount = amount1
                            
                            # Simple heuristic: if description suggests payment/withdrawal, it's debit
                            debit = ''
                            credit = ''
                            
                            if any(word in description.lower() for word in ['payment', 'pay', 'withdraw', 'bill', 'purchase']):
                                debit = transaction_amount
                            else:
                                credit = transaction_amount
                            
                            data.append({
                                'date': formatted_date,
                                'description': description,
                                'debit': debit,
                                'credit': credit,
                                'balance': balance
                            })
            
            return pd.DataFrame(data)
            
        except Exception as e:
            print(f"Parse error: {e}")
            return pd.DataFrame(columns=['date', 'description', 'debit', 'credit', 'balance'])