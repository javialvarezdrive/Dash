# app.py
import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Cargar datasets
gdp_df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')
diabetes_df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/diabetes-vid.csv')

# Asegúrate de verificar las columnas del dataset de diabetes
print(diabetes_df.columns)  # Esto es útil para debug, muestra los nombres de columnas

# Crear gráficos
gdp_fig = px.choropleth(
    gdp_df, 
    locations="CODE",
    color="GDP (BILLIONS)",
    hover_name="COUNTRY",
    color_continuous_scale=px.colors.sequential.Plasma,
    title="World GDP 2014"
)

# Ajustar el gráfico para que utilice columnas correctas
# Cambia el scatter plot para que use columnas que existen en el dataframe
# Aquí usamos 'Glucose' vs 'BMI' como ejemplo
diabetes_fig = px.scatter(
    diabetes_df, 
    x='Glucose', 
    y='BMI',
    size='Age',  # Puedes ajustar esta parte para representar otra variable
    color='Outcome',  # Categoría binaria para el outcome
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
    app.run_server(debug=True, host='0.0.0.0', port=8050)
