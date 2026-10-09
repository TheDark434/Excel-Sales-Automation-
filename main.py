from src.loader import loader
from src.validator import validate
from src.cleaner import clean_data
from src.analyzer import analyze_data
from src.report import generate_report
from src.formatter import format_report
from src.charts import create_branch_revenue_chart, create_product_quantity_chart, create_category_revenue_chart
from src.cleaned_data_exporter import create_cleaned_workbook
from src.dashboard import create_dashboard

raw_data = loader()
validate(raw_data)
cleaned_data = clean_data(raw_data)
analyzed_data = analyze_data(cleaned_data)
generated_report = generate_report(analyzed_data)


print(analyzed_data["total_revenue"])
print(analyzed_data["branch_revenue_total"])
print(analyzed_data["top_selling_product_quantity"])
format_report()
create_branch_revenue_chart()
create_product_quantity_chart()
create_category_revenue_chart()
create_cleaned_workbook(cleaned_data)
create_dashboard()