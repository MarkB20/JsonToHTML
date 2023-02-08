import os

from converter import converter

Input = os.path.expanduser("~/devops-automation/change_lists")
Output = os.path.expanduser("~/dev-auto-test")
converter(Input, Output)
