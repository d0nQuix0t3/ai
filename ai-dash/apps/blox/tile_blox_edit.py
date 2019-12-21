import dash
import dash_core_components as dcc
import dash_html_components as html

def tile_fx(tile_id):
    tile_id_str = 'tile_input_' + str(tile_id)
    txt = dcc.Dropdown(
        id=tile_id_str,
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montreal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='NYC'
    )
    
    val = "Tile " + str(tile_id)
    return txt, val

def blox_main(tile_id):
    txt, val = tile_fx(tile_id)
    return txt, val