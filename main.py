import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Загрузка данных из csv файла
df = pd.read_csv('C:\Data\посещение.csv')

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

    # Линейный график
    line_chart = px.line(filtered_df, x='Время', y='Просмотры товаров', title='Просмотры товаров по времени')

    # Гистограмма
    histogram = px.histogram(df, x='Время на сайте', title='Распределение времени на сайте')

    # Круговая диаграмма
    pie_chart = px.pie(df, names='Браузер', title='Использование браузеров')

    # Ящик
    box_plot = px.box(df, y='Возраст', title='Возрастные группы пользователей')

    # Точечный график
    scatter_plot = px.scatter(df, x='Возраст', y='Покупки', color='Пол', title='Возраст и покупки')

    return line_chart, histogram, pie_chart, box_plot, scatter_plot

# Запуск приложения
if __name__ == '__main__':
    app.run_server(debug=True)
