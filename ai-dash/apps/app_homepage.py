import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, ClientsideFunction

#APP CONFIG
#########################################################################################################################################
from app import app
from app import page_logo

from . import app_templates, app_controls
page_layout = html.Div(children=[
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
                                    "WELCOME TO AI DASH",
                                    id='page-title',
                                    style={"margin-bottom": "0px"},
                                ),
                                html.H5(
                                    "Dashboards, Reporting, Machine Learning Made Easy", 
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
                            html.Button("AI DASH", id="learn-more-button"),
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
                html.Div([
                        html.P('CREATE PAGE', className="tileHeader"), 
                        html.P('Create Dashboard Pages Quickly!'),
                        html.Br(),
                        html.A(html.Button('CREATE'), href='/apps/create-page',style={'text-align': 'center'})
                    ]
                    ,className="pretty_container four columns"),
                html.Div([
                        html.P('CONFIGURED PAGES', className="tileHeader"), 
                        html.P('View Configred Pages!'),
                        html.Br(),
                        html.A(html.Button('VIEW'), href='/apps/configured-urls',style={'text-align': 'center'})
                    ]
                    ,className="pretty_container four columns"),
                html.Div([
                        html.P('BUILD BLOX', className="tileHeader"), 
                        html.P('Create Fundamental Blox for Pages!'),
                        html.Br(),
                        html.A(html.Button('BUILD'), href='/apps/create-page',style={'text-align': 'center'})
                    ]
                    ,className="pretty_container four columns"),
            ],
            className="row flex-display",
        ), 

        
    ],className='container-builder')

