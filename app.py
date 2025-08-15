import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# Load cleaned_sales.csv
df = pd.read_csv('data/cleaned_sales.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

# Create line chart (sales over time)
fig = px.line(
    df,
    x='date',
    y='sales',
    title='Pink Morsels Sales Over Time'
)
fig.update_layout(
    xaxis_title='Date',
    yaxis_title='Sales'
)

# Initialize Dash app
app = Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("Pink Morsels Sales Visualiser"),
    dcc.Graph(figure=fig)
])

# Run server
if __name__ == "__main__":
    app.run(debug=True)
