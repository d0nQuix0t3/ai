import pandas as pd

def blox_extract():
    blox_data = {
        'column_1': 1,
        'column_2': 2,
        'column_3': 3,
        'column_4': 4
    }
    return blox_data

def blox_transform(b_e):
    blox_data_t = pd.DataFrame(b_e)
    return blox_data_t

def blox_load(b_t):
    blox_data_l = "FIGRE"
    return blox_data_l

def blox_main():
    data = blox_extract()
    transform = blox_transform(data)
    chart = blox_load()
    return chart