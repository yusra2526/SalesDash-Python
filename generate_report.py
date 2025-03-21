import pdfkit
import pandas as pd

# Load cleaned data
df = pd.read_csv("cleaned_sales_data.csv")

# Generate HTML report
html_report = f"""
<html>
<head><title>Sales Report</title></head>
<body>
    <h1>Sales Analysis Report</h1>
    <h2>Summary</h2>
    {df.describe().to_html()}
    <h2>Top Sales Records</h2>
    {df.nlargest(5, 'Sales').to_html()}
</body>
</html>
"""

# Save as an HTML file
with open("sales_report.html", "w") as file:
    file.write(html_report)

# Convert HTML to PDF
pdfkit.from_file("sales_report.html", "sales_report.pdf")

print("PDF Report Generated: sales_report.pdf")
