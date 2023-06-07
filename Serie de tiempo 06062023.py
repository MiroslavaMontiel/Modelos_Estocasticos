import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Especifica la ruta completa del archivo de Excel
ruta_archivo1 = "C:/Users/Miros/Downloads/Archivos 2023 Pcolab/Enero_PColab 2023.xlsx"
ruta_archivo2 = "C:/Users/Miros/Downloads/Archivos 2023 Pcolab/Febrero_PColab 2023.xlsx"
ruta_archivo3 = "C:/Users/Miros/Downloads/Archivos 2023 Pcolab/Marzo_PColab 2023.xlsx"
ruta_archivo4 = "C:/Users/Miros/Downloads/Archivos 2023 Pcolab/Abril_PColab 2023.xlsx"
# Lee el archivo de Excel y asigna los datos a un DataFrame
df1 = pd.read_excel(ruta_archivo1)
df2 = pd.read_excel(ruta_archivo2)
df3 = pd.read_excel(ruta_archivo3)
df4 = pd.read_excel(ruta_archivo4)
# Filtrar las columnas deseadas
columnas_deseadas = ['Productos','PrecioTiendaB', 'TiendaB2', 'PrecioTiendaA2', 'TiendaA2', 'Fecha']
df1_filtrado = df1.filter(columnas_deseadas)
df2_filtrado = df2.filter(columnas_deseadas)
df3_filtrado = df3.filter(columnas_deseadas)
df4_filtrado = df4.filter(columnas_deseadas)
# Info del DataFrame filtrado

# La función append() permite agregar filas adicionales a un DataFrame existente.
#De esta manera, los DataFrames se agregarán uno debajo del otro, como nuevos registros en el DataFrame df_actualizado.
# Crear un DataFrame vacío
df_2023= pd.DataFrame()

# Agregar los DataFrames como registros
import pandas as pd

# Concatenar los DataFrames
df_2023 = pd.concat([df_2023, df1_filtrado, df2_filtrado, df3_filtrado, df4_filtrado], ignore_index=True)

# Ordenar por Fecha ascendente
df_2023 = df_2023.sort_values(by='Fecha', ascending=True)

#Filtros Productos
# Aceite Mixto
df_aceite = df_2023[df_2023['Productos'].str.contains('aceite', case=False)]

# Arroz Largo
df_arroz = df_2023[df_2023['Productos'].str.contains('arroz largo', case=False)]

# Azúcar Estándar
df_azucar = df_2023[df_2023['Productos'].str.contains('Azúcar Estándar', case=False)]

# Harina de Trigo
df_harina = df_2023[df_2023['Productos'].str.contains('Harina de Trigo', case=False)]

# Frijol Flor de Mayo
df_frijolmay = df_2023[df_2023['Productos'].str.contains('Frijol Flor de Mayo', case=False)]

# Frijol Negro
df_frijolnegro = df_2023[df_2023['Productos'].str.contains('Frijol Negro', case=False)]

# Huevo Blanco
df_huevo = df_2023[df_2023['Productos'].str.contains('Huevo Blanco', case=False)]

# Carne Molida Sirloin 90-10
df_carnemolida = df_2023[df_2023['Productos'].str.contains('Carne Molida\nSirloin 90-10', case=False)]

# Bistec Diezmillo de Res
df_bistec = df_2023[df_2023['Productos'].str.contains('Bistec Diezmillo de\nRes', case=False)]

# Aguacate Hass
df_aguacate = df_2023[df_2023['Productos'].str.contains('Aguacate Hass', case=False)]

# Limón con semilla
df_limon = df_2023[df_2023['Productos'].str.contains('Limón con semilla', case=False)]

# Guayaba
df_guayaba = df_2023[df_2023['Productos'].str.contains('Guayaba', case=False)]

# Manzana Golden
df_manzana = df_2023[df_2023['Productos'].str.contains('Manzana Golden', case=False)]

# Manzana Starking
df_manzana2 = df_2023[df_2023['Productos'].str.contains('Manzana Starking', case=False)]

# Naranja mediana
df_naranja = df_2023[df_2023['Productos'].str.contains('Naranja mediana', case=False)]

# Papaya maradol
df_papaya = df_2023[df_2023['Productos'].str.contains('Papaya maradol', case=False)]

# Piña
df_pina = df_2023[df_2023['Productos'].str.contains('Piña', case=False)]

#Plátano
df_platano = df_2023[df_2023['Productos'].str.contains('Plátano', case=False)]

#Sandía
df_sandia = df_2023[df_2023['Productos'].str.contains('Sandía', case=False)]

#Calabacita Italiana
df_calabacita = df_2023[df_2023['Productos'].str.contains('Calabacita Italiana', case=False)]

#Huevo Blanco
df_huevo = df_2023[df_2023['Productos'].str.contains('Huevo Blanco', case=False)]


import plotly.graph_objects as go
import pandas as pd
from pmdarima import auto_arima
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO




import pandas as pd
import plotly.graph_objects as go
from pmdarima import auto_arima

# Definir la función para crear las figuras de predicción ARIMA
def create_arima_figure(df, product_name):
    # Obtener la serie de tiempo para el producto específico
    df_product = df[['Fecha', 'PrecioTiendaA2']].copy()
    df_product['Fecha'] = pd.to_datetime(df_product['Fecha'])
    df_product = df_product.groupby('Fecha')['PrecioTiendaA2'].mean().reset_index()

    # Convertir la columna 'Fecha' a tipo de datos de fecha
    df_product['Fecha'] = pd.to_datetime(df_product['Fecha'])

    # Calcular la media del PrecioTienda por día y establecer 'Fecha' como índice
    df_product_mean = df_product.groupby('Fecha')['PrecioTiendaA2'].mean().reset_index().set_index('Fecha')

    # Aplicar auto_arima para determinar los parámetros del modelo ARIMA
    model = auto_arima(df_product_mean, start_p=1, start_q=1, max_p=30, max_q=30, seasonal=True, max_P=5, max_D=2, max_Q=5, m=12, trace=True)

    # Obtener la fecha de inicio del mes siguiente
    start_date = df_product_mean.index.max() + pd.DateOffset(days=1)
    # Obtener la fecha de fin del mes siguiente
    end_date = start_date + pd.DateOffset(months=1) - pd.DateOffset(days=1)

    # Realizar la predicción para el mes siguiente
    forecast, conf_interval = model.predict(n_periods=len(pd.date_range(start_date, end_date, freq='D')), return_conf_int=True)

    # Crear la figura interactiva con Plotly
    fig = go.Figure()

    # Graficar la predicción
    fig.add_trace(go.Scatter(x=pd.date_range(start_date, end_date, freq='D'), y=forecast, mode='lines+markers', name='Predicción'))

    # Rellenar el intervalo de confianza
    fig.add_trace(go.Scatter(x=pd.date_range(start_date, end_date, freq='D'), y=conf_interval[:, 0], mode='lines', fill=None, line=dict(color='rgba(128, 128, 128, 0.3)'), showlegend=False))
    fig.add_trace(go.Scatter(x=pd.date_range(start_date, end_date, freq='D'), y=conf_interval[:, 1], mode='lines', fill='tonexty', fillcolor='rgba(128, 128, 128, 0.3)', line=dict(color='rgba(128, 128, 128, 0.3)'), showlegend=False))

    # Graficar los datos reales
    fig.add_trace(go.Scatter(x=df_product_mean.index, y=df_product_mean['PrecioTiendaA2'], mode='lines+markers', name='Datos reales'))

    # Configurar el diseño de la figura
    fig.update_layout(
        title=f'Predicción de {product_name} para el mes siguiente',
        xaxis=dict(title='Fecha'),
        yaxis=dict(title='PrecioTiendaA2'),
        xaxis_tickformat='%b %Y',
        legend=dict(x=0, y=1),
        hovermode='x'
    )

    return fig


# Obtener las figuras de predicción ARIMA para cada producto
fig_aceite = create_arima_figure(df_aceite, 'Aceite Mixto')
fig_arroz = create_arima_figure(df_arroz, 'Arroz Largo')
fig_azucar = create_arima_figure(df_azucar, 'Azúcar Estándar')
fig_harina = create_arima_figure(df_harina, 'Harina de Trigo')
fig_frijolmay = create_arima_figure(df_frijolmay, 'Frijol Flor de Mayo')
fig_frijolnegro = create_arima_figure(df_frijolnegro, 'Frijol Negro')
fig_huevo = create_arima_figure(df_huevo, 'Huevo Blanco')
fig_carnemolida = create_arima_figure(df_carnemolida, 'Carne Molida Sirloin 90-10')
fig_bistec = create_arima_figure(df_bistec, 'Bistec Diezmillo de Res')
fig_aguacate = create_arima_figure(df_aguacate, 'Aguacate Hass')
fig_limon = create_arima_figure(df_limon, 'Limón con semilla')
fig_guayaba = create_arima_figure(df_guayaba, 'Guayaba')
fig_manzana = create_arima_figure(df_manzana, 'Manzana Golden')
fig_manzana2 = create_arima_figure(df_manzana2, 'Manzana Starking')
fig_naranja = create_arima_figure(df_naranja, 'Naranja mediana')
fig_papaya = create_arima_figure(df_papaya, 'Papaya maradol')
fig_pina = create_arima_figure(df_pina, 'Piña')
fig_platano = create_arima_figure(df_platano, 'Plátano')
fig_sandia = create_arima_figure(df_sandia, 'Sandía')
fig_calabacita = create_arima_figure(df_calabacita, 'Calabacita Italiana')
fig_huevo2 = create_arima_figure(df_huevo, 'Huevo Blanco')

# Crear la aplicación de Dash
app = dash.Dash(__name__)
server = app.server
# Lista de figuras
figuras = [fig_aceite, fig_arroz, fig_azucar, fig_harina, fig_frijolmay, fig_frijolnegro, fig_huevo, fig_carnemolida,
           fig_bistec, fig_aguacate, fig_limon, fig_guayaba, fig_manzana, fig_manzana2, fig_naranja, fig_papaya,
           fig_pina, fig_platano, fig_sandia, fig_calabacita]

# Definir el estado inicial
indice_actual = 0

# Crear el interruptor de tema
theme_switch = ThemeSwitchAIO(aio_id="theme", themes=[dbc.themes.MINTY, dbc.themes.VAPOR])

# Layout del dashboard
app.layout = dbc.Container(
    children=[
        theme_switch,
        html.H1('Dashboard con múltiples gráficos'),
        dcc.Graph(
            id='graph',
            figure=figuras[indice_actual]
        ),
        html.Button('Siguiente', id='boton-siguiente', n_clicks=0)
    ],
    className="m-4 dbc"
)

# Callback para cambiar el gráfico al hacer clic en el botón
@app.callback(
    Output('graph', 'figure'),
    Output("graph", "config"),
    Input('boton-siguiente', 'n_clicks'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value")
)
def actualizar_grafico(n_clicks, toggle):
    global indice_actual
    indice_actual = (indice_actual + 1) % len(figuras)
    
    template = "minty" if toggle else "vapor"
    figuras[indice_actual].update_layout(template=template)
    
    return figuras[indice_actual], {"displayModeBar": False}

# Ejecutar la aplicación de Dash
if __name__ == '__main__':
    app.run_server(debug=True)






    
