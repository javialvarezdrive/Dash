# app.py
import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Cargar datasets
gdp_df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')
diabetes_df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/diabetes-vid.csv')

# Crear gráficos
gdp_fig = px.choropleth(gdp_df, 
                        locations="CODE",
                        color="GDP (BILLIONS)",
                        hover_name="COUNTRY",
                        color_continuous_scale=px.colors.sequential.Plasma,
                        title="World GDP 2014")

diabetes_fig = px.scatter(diabetes_df, 
                          x='Diabetes per 100 adults', 
                          y='Obesity per 100 adults',
                          size='Obesity per 100 adults',
                          color='Country',
                          hover_name='Country',
                          title='Diabetes vs Obesity')

# Inicializar la app Dash
app = dash.Dash(__name__)

# Layout de la app
app.layout = html.Div([
    html.H1("Dashboard de Visualización de Datos"),
    html.Div([
        html.H2("World GDP 2014"),
        dcc.Graph(figure=gdp_fig)
    ]),
    html.Div([
        html.H2("Diabetes vs Obesity"),
        dcc.Graph(figure=diabetes_fig)
    ])
])

# Ejecución de la app
if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)
