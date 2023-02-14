import os
import shutil


def copyStyle(Output):
    shutil.copyfile(os.path.dirname(__file__) + '/stylesheet.css', f'{Output}/stylesheet.css')
