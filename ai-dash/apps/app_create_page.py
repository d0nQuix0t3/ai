import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, ClientsideFunction

#APP CONFIG
#########################################################################################################################################
#from .app_config import *
from . import app_models

from app import app
from app import page_logo

from . import app_templates, app_controls

template_dd = [
    {'label': 'dash_cntls_1', 'value': 'dash_cntls_1'}
]

create_page_layout = html.Div(children=[
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
                                    "PAGE BUILDER",
                                    id='page-title',
                                    style={"margin-bottom": "0px"},
                                ),
                                html.H5(
                                    "Create Page", 
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
                            html.Button("BUILDER GUIDE", id="learn-more-button"),
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
            html.Label('Please provide a name for your page:', style={'font-size': '20px', 'text-align': 'left'}),
            dcc.Input(id='page-name', placeholder='Enter Page Name (i.e. "Project Name")', type='text', style={'width': '750px','font-size': '16px'}),
            html.Label('Page Name already taken. Please assign a different name.', id='name-val', style={'visibility': 'hidden'}),
        ],
        style={'width': '750px', 'margin-right': 'auto',
            'margin-left': 'auto', 'text-align': 'center'}),
        html.Br(),
        html.P([
            html.Label('Please provide a secondary header / name for your page:', style={'font-size': '20px', 'text-align': 'left'}),
            dcc.Input(id='page-subname', placeholder='Enter Secondary Page Name (i.e. "Sub Project Name")', type='text', style={'width': '750px','font-size': '16px'}),
            #html.Label('Page Name already taken. Please assign a different name.', id='name-val', style={'visibility': 'hidden'}),
        ],
        style={'width': '750px', 'margin-right': 'auto',
            'margin-left': 'auto', 'text-align': 'center'}),
        html.Br(),

        html.P([
            html.Label('Page URL (Must Be Unique):', style={'font-size': '20px', 'text-align': 'left'}),
            dcc.Input(id='page-url', placeholder='Enter Page URL (i.e. "project-name")', type='text', style={'width': '750px','font-size': '16px'}),
            html.Label('URL already taken. Please assign a different url.', id='url-val', style={'visibility': 'hidden'}),
        ],
        style={'width': '750px', 'margin-right': 'auto',
            'margin-left': 'auto', 'text-align': 'center'}),

        html.Br(),


        html.P([
            html.Label('Template you would like to use:', style={'font-size': '20px', 'text-align': 'left'}),
            dcc.Dropdown(
                id='page-template',
                options=template_dd,
                placeholder='Select Page Template From Drop Down',
                style={'width': '750px', 'font-size': '16px'}
            ),
            html.Label('Please select a template.', id='temp-val', style={'visibility': 'hidden'}),
        ],
        style={'width': '750px', 'margin-right': 'auto',
            'margin-left': 'auto'}),
        # 'margin-left': '40px', 'text-align': 'center'}),

        html.Br(),

        html.P([
            html.Label('Page Description:', style={'font-size': '20px', 'text-align': 'left'}),
            dcc.Textarea(
                id='page-desc',
                placeholder='Enter Page Description (i.e. Project ABC is about xyz and is utilizng the qrs metrics to track overall performance and efficiency of the project.)',
                #value='',
                style={'width': '750px', 'font-size': '16px'}
            ) 
            #dcc.Input(id='template_type3', value="Page URL...", type='text', style={'width': '750px', 'text-align': 'center'}),
        ],
        style={'width': '750px', 'margin-right': 'auto',
            'margin-left': 'auto', 'text-align': 'center'}),
        html.Br(),
        html.P([
            html.Button('Create Page', id='create-page-btn'),
            #dcc.Input(id='template_type3', value="Page URL...", type='text', style={'width': '750px', 'text-align': 'center'}),
        ],
        style={'width': '750px', 'margin-right': 'auto',
            'margin-left': 'auto', 'text-align': 'center'}),

        ],
            #className='input-wrapper'
            ),
        
    ],className='container-builder')


#PAGE ENTITIES CALLBACK
#########################################################################################################################################
@app.callback(
    [
        Output("name-val", "style"),
        Output("url-val", "style"),
        Output("temp-val", "style")
    ],
    [
        Input("page-name", "value"),
        Input("page-subname", "value"),
        Input("page-url", "value"),
        Input("page-template", "value"),
        Input("page-desc", "value"),
        Input("create-page-btn", "n_clicks")
    ]
)
def page_callback(pg_name, pg_subname, pg_url, pg_template, pg_desc, n_clicks):
    default_style = {'visibility': 'hidden'}
    red_style = {'color': 'red', 'font-size':'10px', 'text-align': 'left'}
    pg_name_val = default_style
    pg_url_val = default_style
    pg_template_val = default_style
    if n_clicks is None:
        print("WAITING FOR FORM TO BE SUBMITTED")
    else:
        #prev_count = n_clicks - 1
        val_confirm = True
        if pg_name is None:
            pg_name_val = red_style
            val_confirm = False
        if pg_url is None:
            pg_url_val = red_style
            val_confirm = False
        if pg_template is None:
            pg_template_val = red_style
            val_confirm = False
        if val_confirm:
            print("SEND TO SQLITE")
            page_id = 1
            page_name = pg_name
            page_subname = pg_subname
            page_url = '/' + pg_url.lower()
            page_type = str(pg_template)
            page_description = pg_desc
            page_configured = False
            app_models.create_page(page_id, page_name, page_subname, page_description, page_url, page_type, page_configured)
            print("MOVE TO PAGE (TEMPLATE TO BE CONFIGURED)")

        
    
    return pg_name_val, pg_url_val, pg_template_val