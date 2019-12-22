import dash
import dash_core_components as dcc
import dash_html_components as html

def page_config_block1():
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
    well_status_options = [
        {"label": str(WELL_STATUSES[well_status]), "value": str(well_status)}
        for well_status in WELL_STATUSES
    ]

    well_type_options = [
        {"label": str(WELL_TYPES[well_type]), "value": str(well_type)}
        for well_type in WELL_TYPES
    ]

    page_config_block = [
                        html.P("Controls & Filters:", className="controlsHeader"),
                        html.P(
                            "Filter by construction date (or select range in histogram):",
                            className="control_label",
                        ),
                        dcc.RangeSlider(
                            id="year_slider",
                            min=1960,
                            max=2017,
                            value=[1990, 2010],
                            className="dcc_control",
                        ),
                        html.P("Filter by well status:", className="control_label"),
                        dcc.RadioItems(
                            id="well_status_selector",
                            options=[
                                {"label": "All ", "value": "all"},
                                {"label": "Active only ", "value": "active"},
                                {"label": "Customize ", "value": "custom"},
                            ],
                            value="active",
                            labelStyle={"display": "inline-block"},
                            className="dcc_control",
                        ),
                        dcc.Dropdown(
                            id="well_statuses",
                            options=well_status_options,
                            multi=True,
                            value=list(WELL_STATUSES.keys()),
                            className="dcc_control",
                        ),
                        dcc.Checklist(
                            id="lock_selector",
                            options=[{"label": "Lock camera", "value": "locked"}],
                            className="dcc_control",
                            value=[],
                        ),
                        html.P("Filter by well type:", className="control_label"),
                        dcc.RadioItems(
                            id="well_type_selector",
                            options=[
                                {"label": "All ", "value": "all"},
                                {"label": "Productive only ", "value": "productive"},
                                {"label": "Customize ", "value": "custom"},
                            ],
                            value="productive",
                            labelStyle={"display": "inline-block"},
                            className="dcc_control",
                        ),
                        dcc.Dropdown(
                            id="well_types",
                            options=well_type_options,
                            multi=True,
                            value=list(WELL_TYPES.keys()),
                            className="dcc_control",
                        ),
                    ]
    return page_config_block


def page_config_blox_selector():
    page_config_block = [
                        html.P("Controls & Filters:", className="controlsHeader"),
                        html.Div(style={'height':'80px'}),
                        dcc.Dropdown(
                            id='cont-filt-blox-selector',
                            options=[
                                {'label': 'New York City', 'value': 'NYC'},
                                {'label': 'Montreal', 'value': 'MTL'},
                                {'label': 'San Francisco', 'value': 'SF'}
                            ],
                            value='NYC'
                        ),
                        html.Div(style={'height':'80px'}),
                        
                    ]
    return page_config_block