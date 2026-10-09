from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment

def format_report():
    file_path = r"D:\Projects\Excel Sales Automation\output\sales_report.xlsx"
    workbook = load_workbook(file_path)

# Styles
    header_fill = PatternFill(
    fill_type="solid",
    fgColor="1F4E78"
)

    header_font = Font(
    bold=True,
    color="FFFFFF"
)

    thin_border = Border(
    left=Side(style="thin"),
    right=Side(style="thin"),
    top=Side(style="thin"),
    bottom=Side(style="thin")
)

    center_alignment = Alignment(horizontal="center")

# Format every worksheet
    for sheet in workbook.worksheets:

    # Freeze header
        sheet.freeze_panes = "A2"

    # Format header row
    for cell in sheet[1]:
        cell.fill = header_fill
        cell.font = header_font
        cell.border = thin_border
        cell.alignment = center_alignment

    # Format all cells + borders
    for row in sheet.iter_rows():
        for cell in row:
            cell.border = thin_border

    # Auto-size columns
    for column in sheet.columns:
        max_length = 0
        column_letter = column[0].column_letter

        for cell in column:
            if cell.value is not None:
                max_length = max(max_length, len(str(cell.value)))

        sheet.column_dimensions[column_letter].width = max_length + 3


# Summary formatting
    summary = workbook["Summary"]

    summary["B2"].number_format = '₹#,##0.00'
    summary["B3"].number_format = '#,##0'
    summary["B4"].number_format = '₹#,##0.00'

    for row in range(2, 5):
        summary[f"B{row}"].alignment = center_alignment
  

# Branch Analysis formatting
    branch = workbook["Branch Analysis"]

    for row in range(2, branch.max_row + 1):
        branch[f"B{row}"].number_format = '₹#,##0.00'


# Product Analysis formatting
    product = workbook["Product Analysis"]

    for row in range(2, product.max_row + 1):  
        product[f"B{row}"].number_format = '#,##0'
        product[f"C{row}"].number_format = '₹#,##0.00'


# Category Analysis formatting
    category = workbook["Category Analysis"]

    for row in range(2, category.max_row + 1):
        category[f"B{row}"].number_format = '₹#,##0.00'


    workbook.save(file_path)

print("Excel formatting completed successfully!")

     