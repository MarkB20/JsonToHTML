import json
import os

from json2html import *

from src.beautifulsoup import bs
from src.JsonFormatter import JsonFormatter


def converter(input, output):
    try:
        os.unlink(input + "/dummy.txt")
    except:
        print("no dummy file")
        # goes through each file in the folder
    for file in os.listdir(input):
        # only allowing files that are json files to be read
        jsonFilePath = os.path.expanduser(f"{input}/{file}")
        print(jsonFilePath)
        # if the file is not a json file or is not empty
        with open(jsonFilePath) as f:
            loader = json.load(f)
            # covets the html file and sorts it into the var
            convertedJson = json2html.convert(json=loader)
            # storing the path to the output path to store below
            HTMLFilePath = os.path.expanduser(f"{output}/{file.replace('.json', '')}.html")
        # opens the output file from the var above
        convertedJson = bs(convertedJson)
        with open(HTMLFilePath, 'w') as htmlFile:
            htmlFile.write(str(convertedJson))  # writes the converted json to the output file
            print("json converted")
