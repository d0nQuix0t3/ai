import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, ClientsideFunction

#APP CONFIG
#########################################################################################################################################
from app import app
from app import page_logo

from . import app_templates, app_controls
app_404_layout = html.Div(children=[
        #TITLE BAR
        html.Div(
            [
                html.Div(
                    [
                        html.Img(
                            src=page_logo,
                            id="page-logo-image",
                            style={
                                "height": "60px",
                                "width": "auto",
                                "margin-bottom": "25px",
                            },
                        )
                    ],
                    className="one-third column",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.H3(
                                    "COULD NOT FIND PAGE",
                                    id='page-title',
                                    style={"margin-bottom": "0px"},
                                ),
                                html.H5(
                                    "404", 
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
                            html.Button("HOME", id="learn-more-button"),
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



        html.Br(),

        html.Div([
        
        html.P([
            html.Button('Create Page', id='create-page-btn'),
            #dcc.Input(id='template_type3', value="Page URL...", type='text', style={'width': '500px', 'text-align': 'center'}),
        ],
        style={'width': '500px', 'margin-right': 'auto',
            'margin-left': 'auto', 'text-align': 'center'}),

        ],
            #className='input-wrapper'
            ),
        
    ],className='container-builder')

