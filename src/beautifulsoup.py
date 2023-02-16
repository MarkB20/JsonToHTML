import os

import bs4


def bs(Output):
    # getting the converted json hat has been turned onto html ad adding it into a soup var
    soup = bs4.BeautifulSoup(Output, "html.parser")
    # having each setting as a var
    Path = f'"stylesheet.css"'
    textCss = '"text/css"'
    stylesheet = '"stylesheet"'

    # creating the link tag that wraps around the table, so it can be formatted
    soup.table.wrap(soup.new_tag(f"link href= {Path} rel = {stylesheet} type= {textCss} "))
    soup = soup.prettify()
    return (soup)
