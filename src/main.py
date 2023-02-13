import os

from converter import converter
from src.copyStyle import copyStyle
import config

#Input = os.path.expanduser("~/devops-automation/change_lists")
#Output = os.path.expanduser("~/dev-auto-test")

converter(config.Input, config.Output)
copyStyle(config.Output)
