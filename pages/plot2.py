import dash
from dash import dcc, html, Input, Output, callback
import plotly.express as px

dash.register_page(__name__, path='/plot2')

layout = html.Div([
    html.H4('Life expentancy progression of countries per continents'),
    dcc.Graph(id="plot2"),
    dcc.Checklist(
        id="checklist",
        options=["Asia", "Europe", "Africa","Americas","Oceania"],
        value=["Americas", "Oceania"],
        inline=True
    ),
])

@callback(
    Output("plot2", "figure"),
    Input("checklist", "value"))
def update_line_chart(continents):
    df = px.data.gapminder() # replace with your own data source
    mask = df.continent.isin(continents)
    fig = px.line(df[mask],
        x="year", y="lifeExp", color='country')
    return fig
