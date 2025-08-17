import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# Load cleaned_sales.csv
df = pd.read_csv('cleaned_sales.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

# Initialize Dash app
app = Dash(__name__)

# Layout
app.layout = html.Div([

    html.H1("Pink Morsels Sales Visualiser",
            style={'textAlign': 'center',
                   'color': '#6a1b9a',
                   'font-family': 'Verdana',
                   'margin-bottom': '30px'}),

    # Radio button for region filter
    html.Div([
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': 'all'}
            ],
            value='all',
            labelStyle={'display': 'inline-block',
                        'margin-right': '20px',
                        'font-size': '18px',
                        'cursor': 'pointer',
                        'color': '#333'},
            style={'textAlign': 'center', 'margin-bottom': '25px'}
        )
    ], style={'backgroundColor': '#f3e5f5',
              'padding': '15px',
              'border-radius': '12px',
              'box-shadow': '2px 2px 10px rgba(0,0,0,0.1)',
              'margin-bottom': '30px'}),

    # Graph
    dcc.Graph(id='sales-graph',
              style={'border': '2px solid #6a1b9a',
                     'border-radius': '10px',
                     'padding': '10px',
                     'backgroundColor': 'white'})
],
style={'font-family': 'Verdana',
       'backgroundColor': '#fafafa',
       'padding': '40px'}
)

# Callback to update graph
@app.callback(
    Output('sales-graph', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    if selected_region == 'all':
        dff = df
    else:
        dff = df[df['region'] == selected_region]

    fig = px.line(
        dff,
        x='date',
        y='sales',
        title=f"Pink Morsels Sales Over Time ({selected_region.capitalize()})"
    )
    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Sales',
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(color='#333', family='Verdana'),
        title_x=0.5,
        title_font=dict(size=22, color='#6a1b9a')
    )
    return fig

# Run server
if __name__ == "__main__":
    app.run(debug=True)
