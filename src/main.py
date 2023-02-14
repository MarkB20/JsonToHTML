import os

from converter import converter
from src.copyStyle import copyStyle
import config

converter(config.Input, config.Output)
copyStyle(config.Output)
