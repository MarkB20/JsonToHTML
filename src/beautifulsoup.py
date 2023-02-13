import os


import bs4  # BeautifulSoup 3 has been replaced

import bs4   #BeautifulSoup 3 has been replaced

def bs(Output):
    file = open(Output)
    cssPath=os.path.dirname(__file__)+"/stylesheet.css"
    soup=bs4.BeautifulSoup(file.read(),"html.parser")
    for tag in soup.table.find_all(['table']):
        if tag.text == 'fruit':
            tag.wrap(soup.new_tag('a'))



    #soup.table.string.wrap(soup.new_tag("div"))
    outputFile = open("output.html", "w")
    outputFile.write(str(soup))
    file.close()
    outputFile.close()




