import os

import bs4  # BeautifulSoup 3 has been replaced
# TODO! covert function to return output
# TODO! find the best way to style the tables in the style sheet
import bs4  # BeautifulSoup 3 has been replaced


def bs(Output):
    #file = open(Output)
    cssPath = os.path.dirname(__file__) + "/stylesheet.css"
    #soup = bs4.BeautifulSoup(file.read(), "html.parser")
    soup = bs4.BeautifulSoup(Output, "html.parser")
    # Path = f'"{cssPath}"'
    Path = f'"stylesheet.css"'
    textCss = '"text/css"'
    stylesheet = '"stylesheet"'

    # print(f"<link href= {Path} rel = {stylesheet} type= {textCss} ")

    soup.table.wrap(soup.new_tag(f"link href= {Path} rel = {stylesheet} type= {textCss} "))
    return (soup)

    #soup.table.string.wrap(soup.new_tag("div"))
    #outputFile = open("output.html", "w")
    #outputFile.write(str(soup))
    #file.close()
    #outputFile.close()
