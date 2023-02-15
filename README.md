Subject: [PATCH] README suggestions + small changes to run locally
---
Index: README.md
IDEA additional info:
Subsystem: com.intellij.openapi.diff.impl.patch.CharsetEP
<+>UTF-8
===================================================================
diff --git a/README.md b/README.md
--- a/README.md	(revision 1b81cbf1e2a1adbe8dc5beefbbba87f4e2314409)
+++ b/README.md	(revision a4db7807b3f7053e69bb6fd16a82c81b97e18c38)
@@ -1,5 +1,18 @@
 # JsonToHTML
 
+## Running
+### Prerequisites
+- python3 must be installed.
+- Ensure `pip3` is available to install Python modules.
+- Install module `json2html`: `pip3 install json2html`
+- Install module Beautiful Soup: `pip3 install bs4`
+### Instructions
+- Adjust `config.py` such that input and output directories are specified.
+- Copy `config.py` to the `src` directory.
+- Run as follows: `python3 ./src/main.py`
+
+## Development
 - Currently when implementing this project you will have to change where the files come from and go in the config file.
 
+## Testing
 - When running tests make sure that the file paths are set first in the config file.
Index: src/converter.py
IDEA additional info:
Subsystem: com.intellij.openapi.diff.impl.patch.CharsetEP
<+>UTF-8
===================================================================
diff --git a/src/converter.py b/src/converter.py
--- a/src/converter.py	(revision 1b81cbf1e2a1adbe8dc5beefbbba87f4e2314409)
+++ b/src/converter.py	(revision a4db7807b3f7053e69bb6fd16a82c81b97e18c38)
@@ -1,9 +1,7 @@
 import json
 import os
-
 from json2html import *
-
-from src.beautifulsoup import bs
+import bs4
 
 
 def converter(input, output):
@@ -20,9 +18,7 @@
                 # storing the path to the output path to store below
                 HTMLFilePath = os.path.expanduser(f"{output}/{file.replace('.json', '')}.html")
             # opens the output file from the var above
-            convertedJson = bs(convertedJson)
+            convertedJson = bs4.BeautifulSoup(convertedJson)
             with open(HTMLFilePath, 'w') as htmlFile:
                 htmlFile.write(str(convertedJson))  # writes the converted json to the output file
                 print("json converted")
-
-
Index: src/main.py
IDEA additional info:
Subsystem: com.intellij.openapi.diff.impl.patch.CharsetEP
<+>UTF-8
===================================================================
diff --git a/src/main.py b/src/main.py
--- a/src/main.py	(revision 1b81cbf1e2a1adbe8dc5beefbbba87f4e2314409)
+++ b/src/main.py	(revision a4db7807b3f7053e69bb6fd16a82c81b97e18c38)
@@ -1,8 +1,8 @@
 import config
-from converter import converter
-from src.copyStyle import copyStyle
+import converter
+import copyStyle
 
-# coveting the json files to html files from and to the config designated outputs
-converter(config.Input, config.Output)
+# converting the json files to html files from and to the config designated outputs
+converter.converter(config.Input, config.Output)
 # sends the stylesheet so that the html can look nicer
-copyStyle(config.Output)
+copyStyle.copyStyle(config.Output)
