# -*- coding: utf-8 -*-

__author__ = 'Mayank Tiwari'

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

import dash_html_components as html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

countryDf = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')


@app.callback(
    Output('agg-table', 'children'),
    [Input('year-slider', 'value')])
def generate_table(selected_year):
    dataframe = countryDf[countryDf.year == selected_year]
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), 10))
        ])
    ])


@app.callback(
    Output('life-exp-vs-gdp', 'figure'),
    [Input('year-slider', 'value')])
def update_figure(selected_year):
    filtered_df = countryDf[countryDf.year == selected_year]
    countryFig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                            size="pop", color="continent", hover_name="country",
                            log_x=True, size_max=60)
    countryFig.update_layout(transition_duration=500)
    return countryFig


agricultureDf = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')
app.layout = html.Div(children=[
    dbc.Row(children=[
        dbc.Col(
            children=[
                dcc.Graph(
                    id='life-exp-vs-gdp'
                ),
                dcc.Slider(
                    id='year-slider',
                    min=countryDf['year'].min(),
                    max=countryDf['year'].max(),
                    value=countryDf['year'].min(),
                    marks={str(year): str(year) for year in countryDf['year'].unique()},
                    step=None
                )
            ]
        ),
        dbc.Col(style={'padding': '10px'}, children=[
            html.H4(
                children='Life Exp. Vs GDP/Cap', style={
                    'textAlign': 'center',
                }),
            html.Table(id='agg-table')]
                )]),
])

if __name__ == '__main__':
    app.run_server(debug=True)
