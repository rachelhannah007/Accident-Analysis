# Requires BigML Python bindings
#
# Install via: pip install bigml
#
# or clone it:
#   git clone https://github.com/bigmlcom/python.git
from bigml.cluster import Cluster
from bigml.api import BigML
# Downloads and generates a local version of the cluster, if it
# hasn't been downloaded previously.
cluster = Cluster('cluster/5c5b1e66eba31d588b004809',
                  api=BigML("rshelton",
                            "adabd734dd2a2af5cb4e49176f0eb472cfa8ce5a",
                            domain="bigml.io"))
# To predict centroids fill the desired input_data
# in next line. Numeric fields are compulsory.
input_data = {
    "LATITUDE": 1,
    "LONGITUDE": 1,
    "FID": 1,
    "Hour": 1,
    "YEAR": 1,
    "DATE": 1,
    "Index_": 1,
    "ACCNUM": 1,
    "﻿X": 1,
    "Y": 1,
    "FATAL_NO": 1,
    "DATE.hour": 1,
    "DATE.day-of-month": 1,
    "DATE.day-of-week": 1,
    "DATE.year": 1,
    "DATE.month": 1}
cluster.centroid(input_data)
# The result is a dict with three keys: distance, centroid_name and
# centroid_id
            
