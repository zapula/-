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