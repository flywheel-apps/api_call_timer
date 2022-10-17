from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from . import ids


def render(app: Dash) -> html.Div:
    all_calls = [
        "project",
        "subject",
        "session",
        "acquisition"
    ]

    # @app.callback(
    #     Output(ids.SITE_DROPDOWN, "value"),
    #     Input(ids.SELECT_ALL_NATIONS_BUTTON, "n_clicks"),
    # )
    # def select_all_nations(_: int) -> list[str]:
    #     return all_sites

    return html.Div(
        children=[
            html.H6("Call"),
            dcc.Dropdown(
                id=ids.CALL_DROPDOWN,
                options=[{"label": site, "value": site} for site in all_calls],
                value=all_calls,
                multi=False,
            )
        ]
    )