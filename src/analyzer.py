def analyze_data(data):
    data["Revenue"] = data["Quantity"] * data["Unit_Price"]
    total_revenue = data["Revenue"].sum()
    total_quantity = data["Quantity"].sum()
    average_transaction_value = total_revenue / len(data)

    branch_revenue = data.groupby("branch")
    branch_revenue_total = branch_revenue["Revenue"].sum()

    category_revenue = data.groupby("Category")
    category_revenue_total = category_revenue["Revenue"].sum()

    top_selling_product = data.groupby("Product")
    top_selling_product_quantity = top_selling_product["Quantity"].sum().sort_values(ascending= False)

    product_revenue = data.groupby("Product")
    product_revenue_total = product_revenue["Revenue"].sum().sort_values(ascending= False)







    analysis_results = {
        "data" : data,
        "total_revenue" : total_revenue,
        "total_quantity" : total_quantity,
        "average_transaction_value" : average_transaction_value,
        "branch_revenue_total" : branch_revenue_total,
        "category_revenue_total" : category_revenue_total,
        "top_selling_product_quantity" : top_selling_product_quantity,
        "product_revenue_total" : product_revenue_total

    }
    return analysis_results