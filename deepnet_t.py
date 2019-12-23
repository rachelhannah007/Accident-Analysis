# Requires BigML Python bindings
#
# Install via: pip install bigml
#
# or clone it:
#   git clone https://github.com/bigmlcom/python.git
from bigml.deepnet import Deepnet
from bigml.api import BigML
# Downloads and generates a local version of the DEEPNET,
# if it hasn't been downloaded previously.
deepnet = Deepnet('deepnet/5c59efee00a1e50a6c0039ba',
                  api=BigML("rshelton",
                            "adabd734dd2a2af5cb4e49176f0eb472cfa8ce5a",
                            domain="bigml.io"))
# To make predictions fill the desired input_data in next line.
input_data = {
    "EMERG_VEH": "yes",
    "Division": "d42",
    "DISABILITY": "yes",
    "ACCLASS": "Non-Fatal Injury",
    "RDSFCOND": "Dry",
    "INVTYPE": "Driver",
    "IMPACTYPE": "Turning Movement",
    "ACCLOC": "At Intersection",
    "LIGHT": "Daylight",
    "VISIBILITY": "Clear",
    "Ward_Name": "scarborough",
    "INJURY": "None",
    "INVAGE": "unknown",
    "ALCOHOL": "yes",
    "REDLIGHT": "yes",
    "LOCCOORD": "Intersection",
    "TRUCK": "yes",
    "LATITUDE": 1,
    "LONGITUDE": 1,
    "ROAD_CLASS": "Major Arterial",
    "District": "Toronto East York",
    "AG_DRIV": "yes",
    "OFFSET": "east",
    "PASSENGER": "yes",
    "PEDESTRIAN": "yes",
    "SPEEDING": "yes",
    "PEDACT": "Crossing, no Traffic Control",
    "PEDCOND": "Normal",
    "CYCLISTYPE": "Cyclist without ROW rides into path of motorist at inter, lnwy, dwy-Cyclist not turn.",
    "CYCACT": "Driving Properly",
    "FID": 1,
    "CYCCOND": "Normal",
    "PEDTYPE": "Pedestrian hit at mid-block",
    "Hour": 1,
    "YEAR": 1,
    "DATE": 1,
    "Index_": 1,
    "ACCNUM": 1,
    "﻿X": 1,
    "Y": 1,
    "AUTOMOBILE": "yes",
    "MOTORCYCLE": "yes",
    "CYCLIST": "yes",
    "STREET1": "ave",
    "STREET2": "ave",
    "DRIVACT": "Driving Properly",
    "MANOEUVER": "Going Ahead",
    "DRIVCOND": "Normal",
    "FATAL_NO": 1,
    "VEHTYPE": "automobile",
    "INITDIR": "West",
    "DATE.hour": 1,
    "DATE.day-of-month": 1,
    "DATE.day-of-week": 1,
    "DATE.year": 1,
    "DATE.month": 1
}
deepnet.predict(input_data, full=True)
#
# input_data: dict for the input values
# (e.g. {"petal length": 1, "sepal length": 3})
# full: if set to True, the output will be a dictionary that includes all the
# available information about the prediction. The attributes vary depending
# on the ensemble type. Please check:
# https://bigml.readthedocs.io/en/latest/#local-deepnet-predictions