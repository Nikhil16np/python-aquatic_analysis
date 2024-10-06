import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Load the dataset
df = pd.read_csv('aquatic.csv')

app = dash.Dash(__name__)

# Dropdown options
organism_options = [{'label': organism, 'value': organism} for organism in df['Organism Name'].unique()]

app.layout = html.Div([
    html.H1("Marine Microorganism Data Visualization"),
    
    dcc.Dropdown(
        id='organism-dropdown',
        options=organism_options,
        value=df['Organism Name'].iloc[0],
        clearable=False
    ),
    
    dcc.Graph(id='depth-vs-temperature'),
    
    dcc.Graph(id='ph-vs-oxygen')
])

# Callback to update the graphs based on dropdown selection
@app.callback(
    [dash.dependencies.Output('depth-vs-temperature', 'figure'),
     dash.dependencies.Output('ph-vs-oxygen', 'figure')],
    [dash.dependencies.Input('organism-dropdown', 'value')]
)
def update_graphs(selected_organism):
    filtered_df = df[df['Organism Name'] == selected_organism]
    
    fig1 = px.scatter(filtered_df, x='Depth', y='Temperature',
                      title=f'Depth vs Temperature for {selected_organism}',
                      labels={'Depth': 'Depth (m)', 'Temperature': 'Temperature (°C)'},
                      hover_data=['Chemical Used', 'Energy Source'])
    
    fig2 = px.scatter(filtered_df, x='Ph', y='Oxygen level',
                      title=f'Ph vs Oxygen Level for {selected_organism}',
                      labels={'Ph': 'Ph Level', 'Oxygen level': 'Oxygen Level (mg/L)'},
                      hover_data=['Primary Byproduct'])
    
    return fig1, fig2

if __name__ == '__main__':
    app.run_server(debug=True)
