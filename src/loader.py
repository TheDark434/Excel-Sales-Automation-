import pandas as pd
from pathlib import Path


folder = Path(r"D:\Projects\Excel Sales Automation\Input")

def loader():
    Dataframes = []
    files = list(folder.glob("*.xlsx"))

    if not files:

        raise FileNotFoundError(
            "No Excel files found in the input folder."
        )
    
    for file in folder.glob("*.xlsx"):
        df = pd.read_excel(file)
        branch_name = file.stem
        branch_name = branch_name.replace("Branch_", "")
        branch_name = branch_name.replace("branch_", "")
        df["branch"] = branch_name
        Dataframes.append(df)
    combined_df = pd.concat(Dataframes, ignore_index= True)
    return combined_df

loader() 


