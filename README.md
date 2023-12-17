# JsonToHTML

## Running

### Prerequisites
- `python3` must be installed.
- Ensure `pip3` is available to install Python modules.
- Install module `json2html`: `pip3 install json2html`
- Install module `Beautiful Soup`: `pip3 install bs4`

### Instructions
- Adjust `config.py` such that input and output directories are specified.
- Copy `config.py` to the `src` directory.
- Run as follows: `python3 ./src/main.py`

## Development

Currently when implementing this project you will have to change where the files come from and go in the config file.

## Testing

When running tests make sure that the file paths are set first in the config file.

## Changes

### `src/converter.py`

```python
import json
import os
from json2html import *
import bs4

def converter(input, output):
    # ...
    convertedJson = bs(convertedJson)
    convertedJson = bs4.BeautifulSoup(convertedJson)
    # ...
