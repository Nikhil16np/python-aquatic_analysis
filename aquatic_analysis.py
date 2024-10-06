import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go

# Load dataset (replace 'aquatic.csv' with the actual path to your CSV)
data = pd.read_csv('aquatic.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Aquatic Data Dashboard"),

    # Dropdown to select plots
    dcc.Dropdown(
        id='plot-type',
        options=[
            {'label': 'Ph Histogram', 'value': 'histogram'},
            {'label': 'Oxygen vs Depth Jointplot', 'value': 'jointplot'},
            {'label': 'Oxygen vs Depth KDE', 'value': 'kde'},
            {'label': 'Sample ID vs Ph Jointplot', 'value': 'sample_ph'},
            {'label': 'Correlation Heatmap', 'value': 'heatmap'},
            {'label': 'Sigmoid Function', 'value': 'sigmoid'},
            {'label': 'Longitude Countplot', 'value': 'countplot'}
        ],
        value='histogram'
    ),

    # Placeholder for the plots
    dcc.Graph(id='graph'),
])

# Callback to update the plot based on the selected value
@app.callback(
    Output('graph', 'figure'),
    [Input('plot-type', 'value')]
)
def update_graph(plot_type):
    if plot_type == 'histogram':
        # Ph Histogram
        fig = px.histogram(data, x='Ph', nbins=data['Temperature'].nunique(), title='Ph Histogram')
    elif plot_type == 'jointplot':
        # Scatter plot of Oxygen level vs Depth
        fig = px.scatter(data, x='Oxygen level', y='Depth', title='Oxygen level vs Depth')
    elif plot_type == 'kde':
        # KDE plot using Plotly (Seaborn equivalent)
        fig = px.density_contour(data, x='Oxygen level', y='Depth', title='KDE: Oxygen level vs Depth')
    elif plot_type == 'sample_ph':
        # Scatter plot for Sample ID vs Ph
        fig = px.scatter(data, x='Sample ID', y='Ph', title='Sample ID vs Ph')
    elif plot_type == 'heatmap':
        # Correlation Heatmap
        corr_matrix = data.corr()
        fig = px
