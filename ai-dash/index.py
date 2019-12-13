import os
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import app_config
from apps import app_homepage
from apps import app_404
#from apps import dash_cntls_1
from apps import app_configured_urls
from apps import app_create_page
from apps import app_templates
from apps import app_models

#APP CONFIG
###########################################################################################
app_port = os.environ['DASH_PORT']
app_debug = os.environ['DASH_DEBUG']
###########################################################################################


#APP URL LIST
url_list = ["url{}".format(i) for i in range(100)]
#print(url_list)






#APP WIREFRAME
###########################################################################################
app.title='AI DASH'
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
    html.Div(id="app-page-details")
    
    
])
###########################################################################################






#APP ROUTING CALLBACK
###########################################################################################
@app.callback([
    Output('app-page-details', 'children'),
    Output('page-content', 'children'),
    
],
              [Input('url', 'pathname')])
def display_page(pathname):

    #LOOK UP PAGE ID BY URL
    page_id = 0
    page_name = "404"
    page_url = pathname
    page_type = "UNKNOWN"
    page_mode = "LIVE"
    
    #PAGE DETAILS HTML BLOCK (DEFAULT - 404 / HOME)
    
    #READ PAGES DB AND EXTRACT PAGE DETAILS
    x_df = app_models.page_details()
    



    if pathname == '/apps/home':
        page_id = 0
        page_name = "HOME PAGE"
        page_url = pathname
        page_type = "HOME-PAGE"
        page_mode = "LIVE"
        page_details = app_templates.page_details_block(page_id, page_name, page_url, page_type, page_mode)
        return page_details, app_homepage.page_layout
    elif pathname == '/apps/create-page':
        page_id = 0
        page_name = "CREATE PAGE"
        page_url = pathname
        page_type = "CREATE-PAGE"
        page_mode = "LIVE"
        page_details = app_templates.page_details_block(page_id, page_name, page_url, page_type, page_mode)
        return page_details, app_create_page.create_page_layout 
    elif pathname == '/apps/configured-urls':
        page_id = 0
        page_name = "CONFIGURED URLS"
        page_url = pathname
        page_type = "CONFIGURED-URLS"
        page_mode = "LIVE"
        page_details = app_templates.page_details_block(page_id, page_name, page_url, page_type, page_mode)
        return page_details, app_configured_urls.page_layout
    else:
        if len(x_df.index) > 0:
            page_details, url_page_layout = app_config.app_url_router(pathname, x_df)
        else:
            page_details = app_templates.page_details_block(page_id, page_name, page_url, page_type, page_mode)
            url_page_layout = app_404.app_404_layout
        return page_details, url_page_layout
###########################################################################################





#APP MAIN
###########################################################################################
if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=app_port, debug=True)
###########################################################################################