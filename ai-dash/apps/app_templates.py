import dash
import dash_core_components as dcc
import dash_html_components as html

def page_details_block(page_id, page_name, page_url, page_type, page_mode):
    page_id_options = [{'label': 'PAGE ID: {}'.format(page_id), 'value': page_id}]
    page_id_value = [page_id]
    page_name_options = [{'label': 'PAGE NAME: {}'.format(page_name), 'value': page_name}]
    page_name_value = [page_name]
    page_url_options = [{'label': 'PAGE URL: {}'.format(page_url), 'value': page_url}]
    page_url_value = [page_url]
    page_type_options = [{'label': 'PAGE TYPE: {}'.format(page_type), 'value': page_type}]
    page_type_value = [page_type]
    page_mode_options = [{'label': 'PAGE MODE: {}'.format(page_mode), 'value': page_mode}]
    page_mode_value = [page_mode]

    page_details=[
            dcc.Checklist(
                id="app-page-id",
                options=page_id_options,
                value=page_id_value
            ),
            dcc.Checklist(
                id="app-page-name",
                options=page_name_options,
                value=page_name_value
            ),
            dcc.Checklist(
                id="app-page-url",
                options=page_url_options,
                value=page_url_value
            ),
            dcc.Checklist(
                id="app-page-type",
                options=page_type_options,
                value=page_type_value
            ),
            dcc.Checklist(
                id="app-page-mode",
                options=page_mode_options,
                value=page_mode_value
            ) 
    ]
    return page_details

def row_major_block():
    row_major_block = html.Div(
                    [dcc.Graph(id="row_major_block")],
                    className="pretty_container seven columns",
                )
    return row_major_block

def row_minor_block():
    row_minor_block = html.Div(
                    [dcc.Graph(id="row_minor_block")],
                    className="pretty_container five columns",
                )
    return row_minor_block

def row_full_block():
    row_full_block = html.Div(
                    [dcc.Graph(id="row_full_block")],
                    className="pretty_container thirteen columns",
                )
    return row_full_block

def row_tri_block():
    row_tri_block = html.Div(
                    [dcc.Graph()],
                    className="pretty_container four columns",
                )
    return row_tri_block

def tile_row_1x4(t1_t, t1_v, t2_t, t2_v, t3_t, t3_v, t4_t, t4_v):
    tile_row_1x4 = [html.Div(id="tiles1x4",className="row container-display"),
                    html.Div(
                        [html.H6(t1_v, id="tile1"), html.P(t1_t, className="tileHeader")],
                        id="tile1block",
                        className="mini_container",
                    ),
                    html.Div(
                        [html.H6(t2_v, id="tile2"), html.P(t2_t, className="tileHeader")],
                        id="tile2block",
                        className="mini_container",
                    ),
                    html.Div(
                        [html.H6(t3_v, id="tile3"), html.P(t3_t, className="tileHeader")],
                        id="tile3block",
                        className="mini_container",
                    ),
                    html.Div(
                        [html.H6(t4_v, id="tile4"), html.P(t4_t, className="tileHeader")],
                        id="tile4block",
                        className="mini_container",
                    )]
    return tile_row_1x4 


