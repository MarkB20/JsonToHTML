import json
import os

import config

jsonFilePath = os.path.expanduser(f"{config.Input}/2022.10.05.0.json")
# if the file is not a json file or is not empty
with open(jsonFilePath) as f:
    loader = json.load(f)

for row0 in loader:
    print(row0)
    for temp0 in loader[row0]:
        json_object = json.dumps(temp0, indent=4)
        temp0 = json.loads(json_object)
        if "pr" not in temp0:

            y = {"pr": "N/A"}

            # parsing JSON string:


            # appending the data
            temp0.update(y)

            # the result is a JSON string:

            print(temp0)
            #print(json_object)
            # print(type(temp0))
        else:

            print(temp0)
            var = json.dumps(temp0)
    loader[row0] = loader[row0]+ var.split()
print("============================================")

print(loader)



    #print(row0)

    #print(loader[row0].split('}'))
