"""
Mock PDF generator for SBI bank statement
"""

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
import os

def create_sbi_pdf():
    # Get the absolute path for the PDF file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(current_dir, 'sbi_sample.pdf')
    
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
    
    story.append(Paragraph("STATE BANK OF INDIA", title_style))
    story.append(Paragraph("ACCOUNT STATEMENT", styles['Heading2']))
    story.append(Spacer(1, 12))
    
    # Account details
    story.append(Paragraph("<b>Account Number:</b> 9876543210", styles['Normal']))
    story.append(Paragraph("<b>Account Holder:</b> JANE SMITH", styles['Normal']))
    story.append(Paragraph("<b>Period:</b> 01/01/2024 to 31/01/2024", styles['Normal']))
    story.append(Spacer(1, 20))
    
    # Transaction table
    data = [
        ['Date', 'Transaction Details', 'Debit', 'Credit', 'Balance'],
        ['01/01/2024', 'Opening Balance', '', '25000.00', '25000.00'],
        ['03/01/2024', 'NEFT TRANSFER', '5000.00', '', '20000.00'],
        ['05/01/2024', 'INTEREST EARNED', '', '15.75', '20015.75'],
        ['08/01/2024', 'ATM CASH WITHDRAWAL', '1000.00', '', '19015.75'],
        ['12/01/2024', 'SALARY DEPOSIT', '', '45000.00', '64015.75'],
        ['15/01/2024', 'ONLINE PURCHASE', '2500.00', '', '61515.75'],
        ['20/01/2024', 'DIVIDEND RECEIVED', '', '1200.00', '62715.75']
    ]
    
    table = Table(data, colWidths=[1*inch, 2.5*inch, 1*inch, 1*inch, 1*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
    ]))
    
    story.append(table)
    story.append(Spacer(1, 20))
    story.append(Paragraph("<b>Closing Balance: 62715.75</b>", styles['Normal']))
    
    # Build the PDF
    doc.build(story)
    print(f"SBI PDF created successfully at: {pdf_path}")
    return pdf_path

if __name__ == "__main__":
    create_sbi_pdf()