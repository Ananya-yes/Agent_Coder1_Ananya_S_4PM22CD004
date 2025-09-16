import pandas as pd
import pdfplumber
import re
from datetime import datetime

class SIMPLE_TESTParser:
    def __init__(self):
        self.date_formats = ['%d-%m-%Y', '%d/%m/%Y', '%Y-%m-%d']
        self.amount_pattern = r'\d{1,3}(,\d{3})*(\.\d{2})?'

    def parse(self, pdf_path: str) -> pd.DataFrame:
        try:
            with pdfplumber.open(pdf_path) as pdf:
                text = ''
                for page in pdf.pages:
                    text += page.extract_text()
                lines = text.split('\n')
                data = []
                balance = 0
                for line in lines:
                    if line.strip() and not line.startswith('DATE'):
                        match = re.search(r'(\d{1,2}/\d{1,2}/\d{4}|\d{1,2}-\d{1,2}-\d{4}|\d{4}-\d{1,2}-\d{1,2})', line)
                        if match:
                            date = match.group()
                            for date_format in self.date_formats:
                                try:
                                    date = datetime.strptime(date, date_format).strftime('%Y-%m-%d')
                                    break
                                except ValueError:
                                    pass
                            match = re.search(r'(\d{1,3}(,\d{3})*(\.\d{2})?|\d{1,3}(,\d{3})*(\.\d{2})?)', line)
                            if match:
                                amount = match.group().replace(',', '')
                                if amount:
                                    amount = float(amount)
                            else:
                                amount = None
                            match = re.search(r'([A-Z ]+)', line)
                            if match:
                                description = match.group()
                            else:
                                description = ''
                            if amount:
                                if amount > 0:
                                    debit = amount
                                    credit = 0
                                else:
                                    debit = 0
                                    credit = -amount
                            else:
                                debit = ''
                                credit = ''
                            balance += amount
                            data.append([date, description, debit, credit, balance])
                df = pd.DataFrame(data, columns=['date', 'description', 'debit', 'credit', 'balance'])
                return df
        except Exception as e:
            print(f'Error parsing PDF: {e}')
            return pd.DataFrame()