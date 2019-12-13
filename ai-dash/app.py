import dash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']



app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server

page_logo = app.get_asset_url("img/ai-dash-logo-mini.svg")
edit_img = app.get_asset_url("img/edit.svg")
#fav_icon = app.get_asset_url("ai-dash-favicon.svg")

app.config.suppress_callback_exceptions = True