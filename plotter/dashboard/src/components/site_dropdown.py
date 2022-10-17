from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from . import ids


def render(app: Dash) -> html.Div:
    all_sites = [
        "upenn.flywheel.io",
        "ga.ce.flywheel.io",
        "ga.ce.flywheel.io_small",
        "grond.dev.flywheel.io",
        "cni.flywheel.io",
        "wisc.flywheel.io"
    ]

    # @app.callback(
    #     Output(ids.SITE_DROPDOWN, "value"),
    #     Input(ids.SELECT_ALL_NATIONS_BUTTON, "n_clicks"),
    # )
    # def select_all_nations(_: int) -> list[str]:
    #     return all_sites

    return html.Div(
        children=[
            html.H6("Site"),
            dcc.Dropdown(
                id=ids.SITE_DROPDOWN,
                options=[{"label": site, "value": site} for site in all_sites],
                value="",
                multi=True,
            )
        ]
    )
