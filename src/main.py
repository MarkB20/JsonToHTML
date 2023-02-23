import os

import config
from converter import converter
from src.JsonFormatter import JsonFormatter
from src.copyStyle import copyStyle
from test.deleteTest import deleteTest

# TODO! fix header unsticking bug for portal
JsonFormatter(config.Input)
inputJson = "outputJSONFile"
# coveting the json files to html files from and to the config designated outputs
converter(inputJson, config.Output)
# sends the stylesheet so that the html can look nicer
copyStyle(config.Output)

deleteTest(os.path.dirname(__file__) + "/outputJSONFile")
