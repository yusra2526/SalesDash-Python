import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load cleaned data
df = pd.read_csv("cleaned_sales_data.csv")

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Sales Dashboard"),
    dcc.Graph(figure=px.line(df, x="Date", y="Sales", color="Category", title="Sales Over Time")),
    dcc.Graph(figure=px.bar(df, x="Category", y="Sales", title="Total Sales by Category"))
])

if __name__ == "__main__":
    app.run(debug=True)
