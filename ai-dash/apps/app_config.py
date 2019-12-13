import pathlib

from . import app_templates
from . import app_404



APP_VERSION=0.5
APP_DB="app.db"
APP_PATH=pathlib.Path(__file__).parent
APP_DB_PATH=APP_PATH.joinpath(APP_DB).resolve()

def app_url_router(pathname, x_df):
    from . import dash_cntls_1
    #SET DEFAULT RETURN 404/ADD PAGE/HOME
    page_id = 0
    page_name = "404"
    page_url = pathname
    page_type = "UNKNOWN"
    page_mode = "LIVE"
    #PAGE DETAILS HTML BLOCK (DEFAULT - 404 / HOME)
    page_details_default = app_templates.page_details_block(page_id, page_name, page_url, page_type, page_mode)
    url_page_layout = app_404.app_404_layout
    page_found = False
    for i, row in x_df.iterrows():
        x_id = row['page_id']
        x_name = row['page_name']
        x_url = row['page_url']
        x_type = row['page_type']
        x_mode = "LIVE"
        page_details = app_templates.page_details_block(x_id, x_name, x_url, x_type, x_mode)
    
        if pathname == x_url:
            page_found = True
            url_page_layout = dash_cntls_1.page_layout
     
    if page_found:
        return page_details, url_page_layout
    else:
        return page_details_default, url_page_layout
        
    #return 



############################################
COUNTIES = {
    "001": "Albany",
    "003": "Allegany",
    "005": "Bronx",
    "007": "Broome",
    "009": "Cattaraugus",
    "011": "Cayuga",
    "013": "Chautauqua",
    "015": "Chemung",
    "017": "Chenango",
    "019": "Clinton",
    "021": "Columbia",
    "023": "Cortland",
    "025": "Delaware",
    "027": "Dutchess",
    "029": "Erie",
    "031": "Essex",
    "033": "Franklin",
    "035": "Fulton",
    "037": "Genesee",
    "039": "Greene",
    "041": "Hamilton",
    "043": "Herkimer",
    "045": "Jefferson",
    "047": "Kings",
    "049": "Lewis",
    "051": "Livingston",
    "053": "Madison",
    "055": "Monroe",
    "057": "Montgomery",
    "059": "Nassau",
    "061": "New York",
    "063": "Niagara",
    "065": "Oneida",
    "067": "Onondaga",
    "069": "Ontario",
    "071": "Orange",
    "073": "Orleans",
    "075": "Oswego",
    "077": "Otsego",
    "079": "Putnam",
    "081": "Queens",
    "083": "Rensselaer",
    "085": "Richmond",
    "087": "Rockland",
    "089": "St. Lawrence",
    "091": "Saratoga",
    "093": "Schenectady",
    "095": "Schoharie",
    "097": "Schuyler",
    "099": "Seneca",
    "101": "Steuben",
    "103": "Suffolk",
    "105": "Sullivan",
    "107": "Tioga",
    "109": "Tompkins",
    "111": "Ulster",
    "113": "Warren",
    "115": "Washington",
    "117": "Wayne",
    "119": "Westchester",
    "121": "Wyoming",
    "123": "Yates",
}

WELL_STATUSES = dict(
    AC="Active",
    AR="Application Received to Drill/Plug/Convert",
    CA="Cancelled",
    DC="Drilling Completed",
    DD="Drilled Deeper",
    DG="Drilling in Progress",
    EX="Expired Permit",
    IN="Inactive",
    NR="Not Reported on AWR",
    PA="Plugged and Abandoned",
    PI="Permit Issued",
    PB="Plugged Back",
    PM="Plugged Back Multilateral",
    RE="Refunded Fee",
    RW="Released - Water Well",
    SI="Shut-In",
    TA="Temporarily Abandoned",
    TR="Transferred Permit",
    UN="Unknown",
    UL="Unknown Located",
    UM="Unknown Not Found",
    VP="Voided Permit",
)

WELL_TYPES = dict(
    BR="Brine",
    Confidential="Confidential",
    DH="Dry Hole",
    DS="Disposal",
    DW="Dry Wildcat",
    GD="Gas Development",
    GE="Gas Extension",
    GW="Gas Wildcat",
    IG="Gas Injection",
    IW="Oil Injection",
    LP="Liquefied Petroleum Gas Storage",
    MB="Monitoring Brine",
    MM="Monitoring Miscellaneous",
    MS="Monitoring Storage",
    NL="Not Listed",
    OB="Observation Well",
    OD="Oil Development",
    OE="Oil Extension",
    OW="Oil Wildcat",
    SG="Stratigraphic",
    ST="Storage",
    TH="Geothermal",
    UN="Unknown",
)

WELL_COLORS = dict(
    GD="#FFEDA0",
    GE="#FA9FB5",
    GW="#A1D99B",
    IG="#67BD65",
    OD="#BFD3E6",
    OE="#B3DE69",
    OW="#FDBF6F",
    ST="#FC9272",
    BR="#D0D1E6",
    MB="#ABD9E9",
    IW="#3690C0",
    LP="#F87A72",
    MS="#CA6BCC",
    Confidential="#DD3497",
    DH="#4EB3D3",
    DS="#FFFF33",
    DW="#FB9A99",
    MM="#A6D853",
    NL="#D4B9DA",
    OB="#AEB0B8",
    SG="#CCCCCC",
    TH="#EAE5D9",
    UN="#C29A84",
)
