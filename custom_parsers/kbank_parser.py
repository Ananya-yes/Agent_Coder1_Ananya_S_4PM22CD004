import pandas as pd
import pdfplumber
import re
from datetime import datetime

class KBANKParser:
    def __init__(self):
        self.date_formats = ['%d-%m-%Y', '%d/%m/%Y', '%Y-%m-%d']
        self.amount_pattern = r'\d{1,3}(,\d{3})*(\.\d{1,2})?'

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
                    if line.strip() == 'Date Particulars Instrument No Withdrawals Deposits Balance':
                        continue
                    if line.strip() == 'Opening Balance':
                        balance = float(line.split(': ')[1].replace(',', ''))
                        continue
                    match = re.search(r'(\d{1,2}-\d{1,2}-\d{4})', line)
                    if match:
                        date = match.group(0)
                        date = datetime.strptime(date, self.date_formats[0]).strftime('%Y-%m-%d')
                    else:
                        match = re.search(r'(\d{1,2}/\d{1,2}/\d{4})', line)
                        if match:
                            date = match.group(0)
                            date = datetime.strptime(date, self.date_formats[1]).strftime('%Y-%m-%d')
                        else:
                            match = re.search(r'(\d{4}-\d{1,2}-\d{1,2})', line)
                            if match:
                                date = match.group(0)
                                date = datetime.strptime(date, self.date_formats[2]).strftime('%Y-%m-%d')
                            else:
                                date = ''
                    match = re.search(r'UPI:(\w+):(.+?)\((.+?)\)', line)
                    if match:
                        description = match.group(2)
                        if 'Withdrawals' in line:
                            debit = float(re.search(self.amount_pattern, line).group(0).replace(',', ''))
                            credit = 0
                        else:
                            debit = 0
                            credit = float(re.search(self.amount_pattern, line).group(0).replace(',', ''))
                    else:
                        description = line
                        debit = 0
                        credit = 0
                    balance += credit - debit
                    data.append([date, description, debit, credit, balance])
                df = pd.DataFrame(data, columns=['date', 'description', 'debit', 'credit', 'balance'])
                return df
        except Exception as e:
            print(f'Error parsing PDF: {e}')
            return pd.DataFrame()