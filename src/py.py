import os

cssPath = os.path.dirname(__file__) + "/stylesheet.css"
Path = f'"{cssPath}"'
textCss = '"text/css"'
stylesheet = '"stylesheet"'
print(f"<link href= {Path} rel = {stylesheet} type= {textCss} ")
