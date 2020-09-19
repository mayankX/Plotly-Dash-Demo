__author__ = 'Mayank Tiwari'

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.scatter(px.data.iris(), x="sepal_width", y="sepal_length", color="species", title="A Plotly Express Figure")

component1 = dcc.Dropdown(value='MTL', options=[
    {'label': 'New York City', 'value': 'NYC'},
    {'label': 'Montréal', 'value': 'MTL'},
    {'label': 'San Francisco', 'value': 'SF'}])

component2 = dcc.Checklist(value=['MTL'], options=[
    {'label': 'New York City', 'value': 'NYC'},
    {'label': 'Montréal', 'value': 'MTL'},
    {'label': 'San Francisco', 'value': 'SF'}])

component3 = dcc.Slider(min=0, max=9, value=5)

component4 = dcc.Tabs(value='tab-2-example', children=[
    dcc.Tab(label='tab one', value='tab-1-example', children=[
        component1,
        component3
    ]),
    dcc.Tab(label='tab two', value='tab-2-example', children=component2)])

app.layout = html.Div(component4)

if __name__ == '__main__':
    app.run_server(debug=True)
