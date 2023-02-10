import os


import bs4  # BeautifulSoup 3 has been replaced

import bs4   #BeautifulSoup 3 has been replaced

def bs(Output):
    cssPath=os.path.dirname(__file__)+"/stylesheet.css"
    soup=bs4.BeautifulSoup(open(Output).read(),"html.parser")

    soup = f'<link rel="stylesheet"href="{cssPath}>"' + soup.text + f'</link rel="stylesheet"href="{cssPath}>"'
    new = bs4.BeautifulSoup(soup,"html.parser")
    open("output.html", "w").write(str(new))


