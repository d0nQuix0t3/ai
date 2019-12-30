import dash
import dash_core_components as dcc
import dash_html_components as html

def tile_fx(tile_id, blox_selector_list, blox_cur_selection):
    tile_id_str = 'tile_input_' + str(tile_id)
    txt = dcc.Dropdown(
        id=tile_id_str,
        options=[{'label':blox, 'value':blox} for blox in blox_selector_list],
        value=blox_cur_selection
    )
    
    val = "Tile " + str(tile_id)
    return txt, val

def blox_main(tile_id, blox_selector_list, blox_cur_selection):
    txt, val = tile_fx(tile_id, blox_selector_list, blox_cur_selection)
    return txt, val