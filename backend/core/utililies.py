from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate, Spacer, Paragraph
from reportlab.lib.units import inch
from io import BytesIO


def generate_pdf(employee):
    # Extract the necessary fields from the employee object
    full_name = employee.full_name
    department = employee.department
    title = employee.title
    net_salary = employee.net_salary
    salary_advances = employee.salary_advances
    net_balance = employee.net_balance

    # Define the table style
    table_style = TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, 0), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 12),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ("TEXTCOLOR", (0, 1), (-1, -1), colors.black),
        ("ALIGN", (0, 1), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 1), (-1, -1), 12),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 8),
    ])

      # Create a buffer to hold the PDF content
    buffer = BytesIO()

    # Create a list to hold the elements of the document
    elements = []

    # Add a spacer before the table to center it vertically on the page
    elements.append(Spacer(1, 0.5 * inch))

    # Add the table to the elements list
    data = [
        ["Net Salary", str(net_salary)],
        ["Salary Advances", str(salary_advances)],
        ["Net Balance", str(net_balance)],
    ]

    # Create the table object
    table = Table(data)
    table.setStyle(table_style)


    # Add the table to the elements list
    elements.append(table)

    # Set up the document template
    doc = SimpleDocTemplate("balance_slip.pdf", pagesize=letter)

    # Set up the document styles
    styles = getSampleStyleSheet()
    header_style = styles["Heading1"]
    footer_style = styles["Normal"]

    # Add the header to each page
    header_text = "Company Address\n"
    header = Paragraph(header_text, header_style)
    doc.setHeader(header)

    # Add the footer to each page
    footer_text = "Copyright details"
    footer = Paragraph(footer_text, footer_style)
    doc.setFooter(footer)

    # Encrypt the PDF
    password = "mypassword"
    doc.encrypt(password)

    # Build the document
    doc.build(elements)

    # Move the buffer's pointer to the beginning
    buffer.seek(0)

    # Return the PDF content as a file-like object
    return buffer
