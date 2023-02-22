import json
import os

import config


def JsonFormatter(input):
    for file in os.listdir(input):
        jsonFilePath = os.path.expanduser(f"{input}/{file}")
        # if the file is not a json file or is not empty
        if not file.startswith('.') and os.path.isfile(os.path.join(input, file)) and os.stat(
                jsonFilePath).st_size != 0:
            with open(jsonFilePath) as f:
                loader = json.load(f)

            for row0 in loader:

                sub = []
                for temp0 in loader[row0]:

                    json_object = json.dumps(temp0, indent=4)
                    temp0 = json.loads(json_object)
                    if "pr" not in temp0:
                        y = {"pr": "N/A"}
                        temp0.update(y)

                        sub.append(temp0)
                    else:

                        sub.append(temp0)

                loader[row0] = sub

            loader = json.dumps(loader, indent=4)
            output = open(f"outputJSONFile/{file}", 'w')
            output.write(loader)
