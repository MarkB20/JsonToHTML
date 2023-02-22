import config
from converter import converter
from src.copyStyle import copyStyle

# TODO! json formatter so tgat everything is the same

# coveting the json files to html files from and to the config designated outputs
converter(config.Input, config.Output)
# sends the stylesheet so that the html can look nicer
copyStyle(config.Output)
