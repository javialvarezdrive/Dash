import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
import os  # Importar os para acceder a las variables de entorno

# Cargar datasets
gdp_df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')
diabetes_df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/diabetes-vid.csv')

# Crear gráficos
gdp_fig = px.choropleth(
    gdp_df, 
    locations="CODE",
    color="GDP (BILLIONS)",
    hover_name="COUNTRY",
    color_continuous_scale=px.colors.sequential.Plasma,
    title="World GDP 2014"
)

diabetes_fig = px.scatter(
    diabetes_df, 
    x='Glucose', 
    y='BMI',
    size='Age',  
    color='Outcome',  
    hover_name='Age',
    title='Glucose vs BMI'
)

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
        html.H2("Diabetes: Glucose vs BMI"),
        dcc.Graph(figure=diabetes_fig)
    ])
])

# Ejecución de la app
if __name__ == '__main__':
    # Utilizar el puerto definido por Railway o por defecto el 8050
    port = int(os.environ.get('PORT', 8050))
    app.run_server(debug=True, host='0.0.0.0', port=port)
