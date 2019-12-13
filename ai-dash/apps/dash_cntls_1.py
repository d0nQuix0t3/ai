#REQUIREMENTS
#########################################################################################################################################
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, ClientsideFunction

import pandas as pd
import pathlib
import datetime as dt



#APP CONFIG
#########################################################################################################################################
#from .app_config import *

from app import app
from app import page_logo

from . import app_templates, app_controls, app_models

from .blox import default_tile_blox_1 as dtb1
from .blox import default_chart_line as dcl
#from . import blox as blox

#from blox import default_tile_blox_1 as dtb1

# get relative data folder
PATH = pathlib.Path(__file__).parent



# PAGE APP LAYOUT
#########################################################################################################################################
page_layout = html.Div(
    [
        #PAGE STORAGE
        dcc.Store(id="aggregate_data"),
        #TRIGGER JAVASCRIPT FILE FOR GRAPH RESIZING
        html.Div(id="output-clientside"),
        #TITLE BAR
        html.Div(
            [
                html.Div(
                    [
                        html.A(
                        html.Img(
                            src=page_logo,
                            id="page-logo-image",
                            style={
                                "height": "60px",
                                "width": "auto",
                                "margin-bottom": "25px",
                            },
                        ),
                        href='/apps/home')
                    ],
                    className="one-third column",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.H3(
                                    "PAGE TITLE",
                                    id='page-title',
                                    style={"margin-bottom": "0px"},
                                ),
                                html.H5(
                                    "Page Subtitle", 
                                    id='page-subtitle',
                                    style={"margin-top": "0px"}, 
                                    className="pageSubHeader"
                                ),
                            ]
                        )
                    ],
                    className="one-half column",
                    id="title",
                ),
                html.Div(
                    [
                        html.A(
                            html.Button("Learn More", id="learn-more-button"),
                            href="https://plot.ly/dash/pricing/",
                        )
                    ],
                    className="one-third column",
                    id="button",
                ),
            ],
            id="header",
            className="row flex-display",
            style={"margin-bottom": "25px"},
        ),
        html.Div(
            [
                html.Div(id="config-filter-block", className="pretty_container four columns"),
                html.Div(
                    [
                        html.Div(children=[], id="tiles1x4",className="row container-display"),
                        
                        html.Div(
                            [dcc.Graph(id="counXt_graph")],
                            id="main_block_container",
                            className="pretty_container",
                        ),
                    ],
                    id="right-column",
                    className="eight columns",
                ),
            ],
            className="row flex-display",
        ),
        html.Div(id="row1", className="row flex-display"),
        html.Div(id="row2", className="row flex-display"),
        html.Div(id="row3", className="row flex-display"),
        html.Div(id="row4", className="row flex-display"),
        html.Div(id="row5", className="row flex-display"),
        html.Div(id="row6", className="row flex-display"),
        html.Div(id="row7", className="row flex-display"),
        html.Div(id="row8", className="row flex-display"),
        html.Div(id="row9", className="row flex-display"),
        html.Div(id="row10", className="row flex-display"),
        

        #FOOTER - PAGE CALLBACK KEY
        #page_details_block
        dcc.Checklist(
                id="app-page-check",
                options=[
                    {'label': 'PAGE CALLBACK', 'value': 'PAGE'}
                ],
                value=['PAGE']
            ) 
    ],
    id="mainContainer",
    style={"display": "flex", "flex-direction": "column"},
)






#PAGE RESIZING CALLBACK
#########################################################################################################################################
app.clientside_callback(
    ClientsideFunction(namespace="clientside", function_name="resize"),
    Output("output-clientside", "children"),
    [Input("count_graph", "figure")],
)


#PAGE CONTROLS CALLBACK
#########################################################################################################################################
@app.callback(
    Output("aggregate_data", "data"),
    [
        Input("well_statuses", "value"),
        Input("well_types", "value"),
        Input("year_slider", "value"),
    ],
)
def update_production_text(well_statuses, well_types, year_slider):
    return [1, 2, 3]









#PAGE ENTITIES CALLBACK
#########################################################################################################################################
@app.callback(
    [
        Output("page-title", "children"),
        Output("page-subtitle", "children"),
        Output("config-filter-block", "children"),
        Output("tiles1x4", "children"),
        Output("row1", "children"),
        Output("row2", "children"),
        Output("row3", "children"),
        Output("row4", "children"),
        Output("row5", "children"),
        Output("row6", "children"),
        Output("row7", "children"),
        Output("row8", "children"),
        Output("row9", "children"),
        Output("row10", "children")
    ],
    [
        Input("app-page-check", "value"),
        Input("app-page-id", "value"),
        Input("app-page-name", "value"),
        Input("app-page-url", "value"),
        #CONTROL INPUT PLACEHOLDER (AGGREGATE DATA)
    ]
)
def page_callback(app_pg_check, app_pg_id, app_pg_name, app_pg_url):
    print(app_pg_id)
    if app_pg_id[0] > 0:
        page_info = app_models.page_configuration_details(app_pg_id)
    else:
        page_info = {'page_name':'AI DASH', 'page_subname':app_pg_name}


    #PAGE TITLE/SUBTILTE
    page_title = page_info['page_name']
    page_subtitle = page_info['page_subname']

    #CONFIG - FILTER BLOCK
    config_block = app_controls.page_config_block1()

    #TILES
    tile1_text, tile1_value = dtb1.blox_main()
    tile2_text, tile2_value = dtb1.blox_main()
    tile3_text, tile3_value = dtb1.blox_main()
    tile4_text, tile4_value = dtb1.blox_main()
    tile_row = app_templates.tile_row_1x4(tile1_text, tile1_value, tile2_text, tile2_value, tile3_text, tile3_value, tile4_text, tile4_value)

    #ROW 1
    block1 = app_templates.row_major_block()
    block2 = app_templates.row_minor_block()
    row1 = [block1, block2]

    #ROW 2
    block3 = app_templates.row_full_block()
    row2 = block3

    #ROW 3
    block4 = app_templates.row_tri_block()
    block5 = app_templates.row_tri_block()
    block6 = app_templates.row_tri_block()
    row3 = [block4, block5, block6]

    #ROW 4
    row4 = ""

    #ROW 5
    row5 = ""

    #ROW 6
    row6 = ""

    #ROW 7
    row7 = ""

    #ROW 8
    row8 = ""

    #ROW 9
    row9 = ""

    #ROW 10
    row10 = ""



    return page_title, page_subtitle, config_block, tile_row, row1, row2, row3, row4, row5, row6, row7, row8, row9, row10



