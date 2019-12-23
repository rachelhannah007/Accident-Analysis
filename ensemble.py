# Requires BigML Python bindings
#
# Install via: pip install bigml
#
# or clone it:
#   git clone https://github.com/bigmlcom/python.git
from bigml.ensemble import Ensemble
# Downloads and generates a local version of the ensemble, if it
# hasn't been downloaded previously.
from bigml.api import BigML
ensemble = Ensemble('ensemble/5cacf3dceba31d30ba000d60',
                    api=BigML("rshelton",
                              "adabd734dd2a2af5cb4e49176f0eb472cfa8ce5a",
                              domain="bigml.io"))
# To make predictions fill the desired input_data in next line.
input_data = {}
ensemble.predict(input_data, full=True)
#
# input_data: dict for the input values
# (e.g. {"petal length": 1, "sepal length": 3})
# full: if set to True, the output will be a dictionary that includes all the
# available information in the predicted node. The attributes vary depending
# on the ensemble type. Please check:
# https://bigml.readthedocs.io/en/latest/#local-ensemble-s-predictions