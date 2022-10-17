from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import os
import json

from . import ids

base_dir = "/Users/davidparker/Documents/Flywheel/SSE/MyWork/sdk_call_tests/Finder_Tests"

def render(app: Dash) -> html.Div:

    @app.callback(
        Output(ids.SITE_INFO, "children"),
        Input(ids.SITE_DROPDOWN, "value"),
    )
    def update_info(sites: list[str]) -> html.Div:
        site_infos = []
        for site in sites:
            meta_path = os.path.join(base_dir, site, "project_meta.json")
            if os.path.exists(meta_path):
                with open(meta_path, "r") as read_file:
                    meta = json.load(read_file)
                    site_infos.append({site:meta})

        children = []
        for m in site_infos:
            print(m)
            site = list(m.keys())[0]
            m = m[site]
            str_out = []
            print(m)
            for key, val in m.items():
                str_out.append(f"{key}: {val}")
                str_out.append(html.Br())
            children.append(
                html.Div(
                    children=[
                        html.H6(site),
                        html.P(str_out)
                    ],
                    style={'width': '10%','display':'inline-block'}
                )

            )

        return html.Div(
            children=children
        )

    return html.Div(id=ids.SITE_INFO)