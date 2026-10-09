import pandas as pd

def generate_report(analysis_results):

    branch_revenue = analysis_results["branch_revenue_total"]
    total_revenue = analysis_results["total_revenue"]
    total_quantity = analysis_results["total_quantity"]
    average_transaction_value = analysis_results["average_transaction_value"]
    top_selling_product_quantity = analysis_results["top_selling_product_quantity"]
    product_revenue_total = analysis_results["product_revenue_total"]
    category_revenue_total = analysis_results["category_revenue_total"]

    summary = pd.DataFrame({
        "Metric" : ["Total Revenue", "Total Quantity", "Average Transaction Value"],
        "Values" : [total_revenue, total_quantity, average_transaction_value]
    })
                                      
    product_analysis = pd.concat([top_selling_product_quantity , product_revenue_total], axis=1)

    category_analysis = category_revenue_total.reset_index()    
    with pd.ExcelWriter(r"D:\Projects\Excel Sales Automation\output\sales_report.xlsx") as writer:
        branch_revenue.to_excel(writer, sheet_name="Branch Analysis")
        summary.to_excel(writer, sheet_name="Summary", index=False)
        product_analysis.to_excel(writer, sheet_name="Product Analysis", index= True)
        category_analysis.to_excel(writer, sheet_name= "Category Analysis", index = False)