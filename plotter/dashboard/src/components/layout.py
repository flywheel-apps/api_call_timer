from dash import Dash, html

from . import bar_chart, site_dropdown, call_dropdown, site_info


def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className="dropdown-container",
                children=[
                    site_dropdown.render(app),
                    call_dropdown.render(app)
                ],
            ),
            html.Hr(),
            # html.Div(
            #     className='test',
            #     children=[
            #
            #     ]
            # )
            html.Div(
                className="site-info",
                children=site_info.render(app)

            ),
            html.Hr(),
            bar_chart.render(app),
        ],
    )
