
Search




5
Welcome to Mattermost
Let's get up and running.

On Boarding videoWatch overview
🔀 Learn about messaging
👋 Invite team members to the workspace
📱 Download the Desktop and Mobile Apps
📷 Complete your profile
⛰️ Explore other tools in the platform
No thanks, I’ll figure it out myself

Find channel
Insights
Drafts
1

CHANNELS
Copy Link
OpenNMS Development
Copy Link
OpenNMS Discussion
Copy Link
Town Square

DIRECT MESSAGES

Copy Link
2
pierre, thommasmcq
Copy Link
pierre
Copy Link
welcomebot

Invite Members


3



Add a channel header




Start call

At 5:06 PM Wednesday, February 15, pierre replied, This is a patch that can be applied with IntelliJ


This is the start of your group message history with pierre, thommasmcq.
Messages and files shared here are not shown to people outside this area.


Create a board

Set a Header
February 07

pierre
4:58 PM
Function app name driving the status "rings": getApplianceStats

DeviceEndpointFunctions.kt

Specifically of interest: getApplianceStats in DeviceEndpointFunctionsCommon.kt

OverallApplianceState

Yesterday

mbutler
Update your status
2:19 PM
Hi Pierre we have the converter done you just need to change the input and output file to where you want to convert and send the html. the stylesheet can be changed to be anything if you don't like the design.  https://github.com/MarkB20/JsonToHTML 

GitHub
GitHub - MarkB20/JsonToHTML
Contribute to MarkB20/JsonToHTML development by creating an account on GitHub.

GitHub - MarkB20/JsonToHTML

pierre
3:28 PM
Cool, will have a look later today, thanks!

Today
New Messages

pierre
4:08 PM
Hey guys, with a couple minor adjustments, I was able to run your script locally.

The resulting HTML pages look like so - is that expected?



mbutler
Update your status
4:19 PM
that is what it would look like without the stylesheet being copied over into the file so there is a bug there, but roughly yep 


pierre
4:23 PM

I see the CSS got copied over

Didn't see any reference to the CSS from the HTML files


mbutler
Update your status
4:24 PM
more like this, strange so the css file got copied over but the link tag didn't?



pierre
4:28 PM
Ah ok.  Yeah, no luck for me with the stylesheet.  Tried with both Chrome and Firefox


mbutler
Update your status
4:34 PM
so i take it there is no link tag wrapping the html fils then? me and tom will test a couple of different ways then to see if we can get the same error, also out of curiosity what did you change or was it just the config file. thanks for having a look 


mbutler
Update your status
4:56 PM
so we look over what could be wrong and we think it could be the the fact that since the beutifulsoup4 is an external library you may need to install it since it is used to add the link tag to the html. 

also we were think if that is the case, we should add that to the read me or have a script that checks or runs an install for the script. or some other way around it 


pierre
5:05 PM
Already installed it via pip3


pierre
5:05 PM

Since I don't have permissions to push a branch to your repo, here's a few changes I made:

Small-Suggestions.patch
PATCH3KB
Mainly related to the README


pierre
5:06 PM

This is a patch that can be applied with IntelliJ

Login Successful
Write to pierre, thommasmcq












No file chosen


Small-Suggestions.patch
PierreShared In ~Pierre, Thommasmcq

Small-Suggestions.patch - Diff
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
