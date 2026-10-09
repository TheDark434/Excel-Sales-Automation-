import pandas as pd

def clean_data(data):
    data["Customer"] = data["Customer"].str.strip()
    data["Category"] = data["Category"].str.capitalize()
    data["branch"] = data["branch"].str.capitalize()
    data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
    data["Quantity"] = pd.to_numeric(data["Quantity"], errors="coerce")
    data["Unit_Price"] = pd.to_numeric(data["Unit_Price"], errors="coerce")
    data = data.dropna(subset=["Customer", "Date", "Quantity", "Unit_Price"])
    data = data[data["Quantity"] >= 0]
    data = data.drop_duplicates()

    # Check whether any valid data remains
    if data.empty:
        raise ValueError(
            "No valid data remains after cleaning."
        )

    return data



