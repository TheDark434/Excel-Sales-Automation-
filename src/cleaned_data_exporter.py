import pandas as pd
from pathlib import Path

def create_cleaned_workbook(cleaned_data):

    file_path = Path(
    r"D:\Projects\Excel Sales Automation\output\cleaned_sales_data.xlsx"
)

    with pd.ExcelWriter(file_path) as writer:
        cleaned_data.to_excel(writer, sheet_name= "Cleaned Data", index= False)

    print("Cleaned Data has been saved successfully")    
   