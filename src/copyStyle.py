import os
import shutil


def copyStyle(Output):
    # copying the stylesheet to the html output so that the html files can read the html files
    shutil.copyfile(os.path.dirname(__file__) + '/stylesheet.css', f'{Output}/stylesheet.css')
