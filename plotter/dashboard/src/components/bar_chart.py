import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import os

from . import ids

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

API_DATA = pd.read_pickle(os.path.join(BASE_DIR, "data", "df.pkl"))





def render(app: Dash) -> html.Div:
    @app.callback(
        Output(ids.BAR_CHART, "children"),
        Input(ids.SITE_DROPDOWN, "value"),
        Input(ids.CALL_DROPDOWN, "value")
    )
    def update_bar_chart(site: str, calls: list[str]) -> html.Div:
        filtered_data = API_DATA[API_DATA['query'].str.startswith(calls)]
        filtered_data = filtered_data.query("site in @site")

        if filtered_data.shape[0] == 0:
            return html.Div("No data selected.", id=ids.BAR_CHART)

        gb = filtered_data.groupby(['site','query']).mean()
        filtered_data = gb.reset_index()

        fig = px.bar(filtered_data, x="time", y="query", color='site',barmode="group")
        return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)

    return html.Div(id=ids.BAR_CHART)
