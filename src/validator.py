import pandas as pd 

def validate(data):
    column_check = ["Date", "Customer", "Product", "Category", "Quantity", "Unit_Price", "branch"]
    missing_columns = []
    
    if missing_columns:
        raise ValueError(...)

    
    for columns in column_check:
        if columns not in data.columns :
            missing_columns.append(columns)
            print(columns)
    if missing_columns == []:
         print("All columns are present!")

    # missing values
    missing_values = data.isna().any()
    missing_counts = data.isna().sum() 
     
    if (missing_counts != 0).any():
        print(missing_counts[missing_counts != 0])

    # Date Report
    date = pd.to_datetime(data["Date"], errors= "coerce")
    print(date.isna().sum())

    # Quantity Check
    negative_quantities = (data["Quantity"] < 0).sum()
    zero_quantities = (data["Quantity"] == 0).sum()

    invalid_Quantity = pd.to_numeric(data["Quantity"], errors="coerce")
    print(F"Invalid Quantity Input : {invalid_Quantity.isna().sum()}")

    if negative_quantities > 0:
        print(f"Negative quantities found : {negative_quantities}")
    if zero_quantities > 0:
        print(f"Zero quantities found : {zero_quantities}")

    
    # Unit_Price Check
    negative_unit_price = (data["Unit_Price"] < 0).sum()
    zero_unit_price = (data["Unit_Price"] == 0).sum()
    
    if negative_unit_price > 0:
        print(f"Negative Unit_Price found : {negative_unit_price}")
    if zero_unit_price > 0:
        print(f"Zero Unit_Price found : {zero_unit_price }")

    invalid_unit_price = pd.to_numeric(data["Unit_Price"], errors="coerce")
    print(f"Invalid Unit Price Input : {invalid_unit_price.isna().sum()}")

    # Row Check
    duplicate_row_count= data.duplicated().sum()
    if duplicate_row_count > 0:
        print(f"No. of Duplicated rows : {duplicate_row_count}")

    # Row Count Check
    row_count = len(data)
    if row_count != 74 :
        print("Warning! No. of rows is not equal to the No. of actual entries", row_count)
 
 
