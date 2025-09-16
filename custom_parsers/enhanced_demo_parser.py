import pandas as pd
import pdfplumber
import re
from datetime import datetime

class ENHANCED_DEMOParser:
    def __init__(self):
        self.pdf_path = None
        self.pdf_text = None
        self.transactions = []

    def parse(self, pdf_path: str) -> pd.DataFrame:
        self.pdf_path = pdf_path
        try:
            with pdfplumber.open(pdf_path) as pdf:
                self.pdf_text = ''
                for page in pdf.pages:
                    self.pdf_text += page.extract_text()
        except Exception as e:
            print(f"Error parsing PDF: {e}")
            return pd.DataFrame(columns=['date', 'description', 'debit', 'credit', 'balance'])

        self.extract_transactions()
        self.process_transactions()
        self.create_dataframe()

        return pd.DataFrame(self.transactions, columns=['date', 'description', 'debit', 'credit', 'balance'])

    def extract_transactions(self):
        lines = self.pdf_text.splitlines()
        for line in lines:
            if re.search(r'\d{1,2}/\d{1,2}/\d{4}', line):
                date = re.search(r'\d{1,2}/\d{1,2}/\d{4}', line).group()
                description = re.search(r'\D+', line).group()
                debit = re.search(r'\d{1,3}(?:,?\d{3})*(?:\.\d+)?', line)
                credit = re.search(r'\d{1,3}(?:,?\d{3})*(?:\.\d+)?', line)
                if debit and credit:
                    debit = debit.group().replace(',', '')
                    credit = credit.group().replace(',', '')
                else:
                    debit = ''
                    credit = ''
                balance = re.search(r'\d{1,3}(?:,?\d{3})*(?:\.\d+)?', line)
                if balance:
                    balance = balance.group().replace(',', '')
                else:
                    balance = ''
                self.transactions.append([date, description, debit, credit, balance])

    def process_transactions(self):
        for i, transaction in enumerate(self.transactions):
            date = transaction[0]
            description = transaction[1]
            debit = transaction[2]
            credit = transaction[3]
            balance = transaction[4]
            if debit:
                debit = float(debit)
            else:
                debit = 0
            if credit:
                credit = float(credit)
            else:
                credit = 0
            if balance:
                balance = float(balance)
            else:
                balance = 0
            self.transactions[i] = [date, description, debit, credit, balance]

    def create_dataframe(self):
        for i, transaction in enumerate(self.transactions):
            date = transaction[0]
            description = transaction[1]
            debit = transaction[2]
            credit = transaction[3]
            balance = transaction[4]
            if date:
                date = datetime.strptime(date, '%d/%m/%Y').strftime('%Y-%m-%d')
            else:
                date = ''
            if description:
                description = description.strip()
            else:
                description = ''
            if debit:
                debit = str(debit)
            else:
                debit = ''
            if credit:
                credit = str(credit)
            else:
                credit = ''
            if balance:
                balance = str(balance)
            else:
                balance = ''
            self.transactions[i] = [date, description, debit, credit, balance]

if __name__ == "__main__":
    parser = ENHANCED_DEMOParser()
    pdf_path = 'path_to_your_pdf_file.pdf'
    df = parser.parse(pdf_path)
    print(df)