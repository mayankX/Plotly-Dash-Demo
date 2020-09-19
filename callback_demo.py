__author__ = 'Mayank Tiwari'

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')


@app.callback(
    Output('life-exp-vs-gdp', 'figure'),
    Input('year-slider', 'value')
)
def update_figure(selected_year):
    filterDf = df[df.year == selected_year]
    fig = px.scatter(filterDf, x="gdpPercap", y="lifeExp", size="pop", color="continent", hover_name="country", log_x=True, size_max=60)
    fig.update_layout(transition_duration=500)
    return fig


app.layout = html.Div([
    dcc.Graph(id='life-exp-vs-gdp'),
    dcc.Slider(
        id='year-slider', min=df['year'].min(), value=df['year'].min(),
        max=df['year'].max(), marks={str(year): str(year) for year in df['year'].unique()}, step=None
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
