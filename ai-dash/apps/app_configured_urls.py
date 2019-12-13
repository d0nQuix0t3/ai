import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, ClientsideFunction

#APP CONFIG
#########################################################################################################################################
from app import app
from app import page_logo, edit_img

from . import app_templates, app_controls, app_models


def page_links(pages_df):
    link_list = []

    for i, x in pages_df.iterrows():
        
        name = x.page_name
        url = x.page_url

        x_html = html.A(html.Button(name), href=url)
        link_list.append(x_html)
        
    return link_list

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
                                    "AI DASH",
                                    id='page-title',
                                    style={"margin-bottom": "0px"},
                                ),
                                html.H5(
                                    "Configured Pages", 
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
                            html.Button("CREATE PAGE", id="learn-more-button"),
                            href="/apps/create-page",
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
        
        html.P(id='page-urls-configured', 
        style={'width': '900px', 'margin-right': 'auto',
            'margin-left': 'auto', 'text-align': 'center'}),

        ],
            
        ),


        #FOOTER - PAGE CALLBACK KEY
        #page_details_block
        dcc.Checklist(
                id="app-page-check",
                options=[
                    {'label': 'PAGE CALLBACK', 'value': 'PAGE'}
                ],
                value=['PAGE']
            )
    ],className='container-builder')

#PAGE ENTITIES CALLBACK
#########################################################################################################################################
@app.callback(
    [
        Output("page-urls-configured", "children"),
    ],
    [
        Input("app-page-check", "value"),
    ]
)
def page_callback(pg_check):
    pages_df = app_models.page_details()
    link_list = []
    x_count = 0

    for i, x in pages_df.iterrows():
        if x_count >0:
            link_list.append(html.Br())
        name = x.page_name
        subname = x.page_subname
        desc = x.page_description
        url = x.page_url
        ed_url = url + '/edit'

        x_html = html.Div([
            html.Div(
                        [

                            html.H2(name),
                            html.P(subname, className="tileHeader"),
                            html.P(desc),
                            html.Br(),
                            html.Div([
                                        html.Br(),
                                        html.A(html.Button('View'), href=url,style={'text-align': 'center'}),
                                        html.A(html.Button(
                                            html.Img(
                                            src=edit_img,
                                            style={
                                                "height": "12px",
                                                "width": "auto",
                                            },
                                        )
                                        ), href=ed_url,style={'text-align': 'center'})
                                    ],
                                className="row flex",
                                style={'width': '600px','margin-right': 'auto','margin-left': 'auto', 'text-align': 'center'}
                            )
                            
                        ],
                        className="mini_container",
                    ),
            
            ])
        link_list.append(x_html)
        x_count = x_count + 1

    return [link_list]