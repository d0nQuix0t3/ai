#REQUIREMENTS
#########################################################################################################################################
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_daq as daq

import pandas as pd
import pathlib
import datetime as dt



#APP CONFIG
#########################################################################################################################################
#from .app_config import *

from app import app
from app import page_logo

from . import app_templates, app_controls, app_models, app_config

from .blox import default_tile_blox_1 as dtb1
from .blox import tile_blox_edit as tbe
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
        dcc.Store(id="page-controller-data-edit"),
        #TRIGGER JAVASCRIPT FILE FOR GRAPH RESIZING
        html.Div(id="output-clientside-edit"),
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
                                    id='page-title-edit',
                                    style={"margin-bottom": "0px"},
                                ),
                                html.H5(
                                    "Page Subtitle", 
                                    id='page-subtitle-edit',
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
                html.Div(id="config-filter-block-edit", className="pretty_container four columns"),
                html.Div(
                    [
                        html.Div(children=[], id="tiles1x4-edit",className="row container-display"),
                        
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
        html.Div(id="row1-edit", className="row flex-display"),
        html.Div(id="row2-edit", className="row flex-display"),
        html.Div(id="row3-edit", className="row flex-display"),
        html.Div(id="row4-edit", className="row flex-display"),
        html.Div(id="row5-edit", className="row flex-display"),
        html.Div(id="row6-edit", className="row flex-display"),
        html.Div(id="row7-edit", className="row flex-display"),
        html.Div(id="row8-edit", className="row flex-display"),
        html.Div(id="row9-edit", className="row flex-display"),
        html.Div(id="row10-edit", className="row flex-display"),
        
        #FOOTER - LIVE / EDIT
        daq.BooleanSwitch(
            id='edit-toggle',
            on=True,
            label='CONFIGURE',
            labelPosition='bottom'
        ),
        
        #FOOTER - PAGE CALLBACK KEY
        #page_details_block
        dcc.Checklist(
                id="app-page-check-edit",
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
    Output("output-clientside-edit", "children"),
    [Input("count_graph", "figure")],
)


#PAGE CONTROLS CALLBACK
#########################################################################################################################################
@app.callback(
    Output("page-controller-data-edit", "data"),
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
        Output("page-title-edit", "children"),
        Output("page-subtitle-edit", "children"),
        Output("config-filter-block-edit", "children"),
        Output("tiles1x4-edit", "children"),
        Output("main_block_container", "children"),
        Output("row1-edit", "children"),
        Output("row2-edit", "children"),
        Output("row3-edit", "children"),
        Output("row4-edit", "children"),
        Output("row5-edit", "children"),
        Output("row6-edit", "children"),
        Output("row7-edit", "children"),
        Output("row8-edit", "children"),
        Output("row9-edit", "children"),
        Output("row10-edit", "children")
    ],
    [
        Input("app-page-check-edit", "value"),
        Input("app-page-id", "value"),
        Input("app-page-name", "value"),
        Input("app-page-url", "value"),
        Input("edit-toggle", "on")
        #Input("page-controller-data", "data")
        #CONTROL INPUT PLACEHOLDER (AGGREGATE DATA)
    ]
)
def page_callback(app_pg_check, app_pg_id, app_pg_name, app_pg_url, live_edit_toggle):
    
    if app_pg_id[0] > 0:
        page_info = app_models.page_configuration_details(app_pg_id)
    else:
        page_info = {'page_name':'AI DASH', 'page_subname':app_pg_name}


    #PAGE TITLE/SUBTILTE
    page_title = page_info['page_name']
    page_subtitle = page_info['page_subname']
    
    ########################################################################################
    blox_selector_list = app_config.blox_selector_list()
    
    #CONFIG - FILTER BLOCK
    blox_cur_selection = ""
    config_block = app_controls.page_config_blox_selector(blox_selector_list, blox_cur_selection)
    

    #TILES
    tile1_text, tile1_value = tbe.blox_main(1, blox_selector_list, blox_cur_selection)
    tile2_text, tile2_value = tbe.blox_main(2, blox_selector_list, blox_cur_selection)
    tile3_text, tile3_value = tbe.blox_main(3, blox_selector_list, blox_cur_selection)
    tile4_text, tile4_value = tbe.blox_main(4, blox_selector_list, blox_cur_selection)
    
    tile_row = app_templates.tile_row_1x4(tile1_text, tile1_value, tile2_text, tile2_value, tile3_text, tile3_value, tile4_text, tile4_value)

    #MAIN CHART
    main_chart = dcc.Graph(id="counXt_graph")
    main_chart = app_templates.main_chart_blox_selector(0, blox_selector_list, blox_cur_selection)

    #ROW 1
    #block1 = app_templates.row_major_block()
    block1 = app_templates.row_major_blox_selector(1, blox_selector_list, blox_cur_selection)
    block2 = app_templates.row_minor_blox_selector(2, blox_selector_list, blox_cur_selection)
    row1 = [block1, block2]

    #ROW 2
    block3 = app_templates.row_full_blox_selector(3, blox_selector_list, blox_cur_selection)
    row2 = block3

    #ROW 3
    block4 = app_templates.row_tri_blox_selector(4, blox_selector_list, blox_cur_selection)
    block5 = app_templates.row_tri_blox_selector(5, blox_selector_list, blox_cur_selection)
    block6 = app_templates.row_tri_blox_selector(6, blox_selector_list, blox_cur_selection)
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



    return page_title, page_subtitle, config_block, tile_row, main_chart, row1, row2, row3, row4, row5, row6, row7, row8, row9, row10



