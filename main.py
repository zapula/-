import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Загрузка данных из csv файла
df = pd.read_csv('C:\Data\website_data.csv')  # Укажите здесь путь к вашему файлу

# Создание экземпляра приложения
app = dash.Dash(__name__)

# Определение структуры дашборда
app.layout = html.Div([
    html.H1('Анализ данных о посещении веб-сайта', style={'textAlign': 'center'}),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': date, 'value': date} for date in df['Дата'].unique()],
        value=df['Дата'].iloc[0],
        clearable=False,
        style={'width': '50%', 'margin': '0 auto'}
    ),
    dcc.Graph(id='line-chart'),
    dcc.Graph(id='histogram'),
    dcc.Graph(id='pie-chart'),
    dcc.Graph(id='box-plot'),
    dcc.Graph(id='scatter-plot')
], style={'padding': '20px'})

# Определение логики дашборда
@app.callback(
    Output('line-chart', 'figure'),
    Output('histogram', 'figure'),
    Output('pie-chart', 'figure'),
    Output('box-plot', 'figure'),
    Output('scatter-plot', 'figure'),
    [Input('dropdown', 'value')]
)
def update_charts(selected_date):
    filtered_df = df[df['Дата'] == selected_date]

    # Линейный график для просмотров товаров
