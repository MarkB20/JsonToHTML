import shutil


def copyStyle(Output):
    shutil.copyfile('stylesheet.css', f'{Output}/stylesheet.css')
