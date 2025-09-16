"""
Mock PDF generator for ICICI bank statement
This creates a simple PDF file that can be used for testing the parser
"""

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
import os

def create_icici_pdf():
    # Get the absolute path for the PDF file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(current_dir, 'icici_sample.pdf')
    
    # Create the PDF document
    doc = SimpleDocTemplate(pdf_path, pagesize=letter)
    styles = getSampleStyleSheet()
    
    # Create story (content) list
    story = []
    
    # Title
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=16,
        spaceAfter=30,
        alignment=1  # Center alignment
    )
    
    story.append(Paragraph("ICICI BANK LIMITED", title_style))
    story.append(Paragraph("Account Statement", styles['Heading2']))
    story.append(Spacer(1, 12))
    
    # Account details
    story.append(Paragraph("<b>Account Number:</b> 1234567890", styles['Normal']))
    story.append(Paragraph("<b>Account Holder:</b> JOHN DOE", styles['Normal']))
    story.append(Paragraph("<b>Statement Period:</b> 01/01/2024 to 31/01/2024", styles['Normal']))
    story.append(Spacer(1, 20))
    
    # Transaction table
    data = [
        ['DATE', 'DESCRIPTION', 'DEBIT', 'CREDIT', 'BALANCE'],
        ['01/01/2024', 'Opening Balance', '', '50000.00', '50000.00'],
        ['02/01/2024', 'UPI-AMAZON PAY', '1500.00', '', '48500.00'],
        ['03/01/2024', 'SALARY CREDIT', '', '75000.00', '123500.00'],
        ['05/01/2024', 'ATM WITHDRAWAL', '2000.00', '', '121500.00'],
        ['07/01/2024', 'ONLINE TRANSFER TO SAVINGS', '5000.00', '', '116500.00'],
        ['10/01/2024', 'INTEREST CREDIT', '', '125.50', '116625.50'],
        ['15/01/2024', 'ELECTRICITY BILL', '3200.00', '', '113425.50'],
        ['20/01/2024', 'UPI-GROCERIES', '850.00', '', '112575.50'],
        ['25/01/2024', 'DIVIDEND CREDIT', '', '2500.00', '115075.50']
    ]
    
    table = Table(data, colWidths=[1*inch, 2.5*inch, 1*inch, 1*inch, 1*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
    ]))
    
    story.append(table)
    story.append(Spacer(1, 20))
    story.append(Paragraph("<b>Closing Balance: 115075.50</b>", styles['Normal']))
    
    # Build the PDF
    doc.build(story)
    print(f"PDF created successfully at: {pdf_path}")
    return pdf_path

if __name__ == "__main__":
    create_icici_pdf()