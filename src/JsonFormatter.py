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

            # goes through each table
            for table in loader:
                # use for storing each row into a new table to be inserted
                sub = []
                for row in loader[table]:

                    json_object = json.dumps(row, indent=4)
                    row = json.loads(json_object)
                    # checks if the row has a pr attached to it
                    if "pr" not in row:
                        y = {"pr": "N/A"}
                        row.update(y)
                        # appends the table so that it has a row
                        sub.append(row)
                    else:
                        # adds the row that already has a pr
                        sub.append(row)
                # replaces the old table with the new table
                loader[table] = sub

            loader = json.dumps(loader, indent=4)
            # outputs the table
            output = open(f"outputJSONFile/{file}", 'w')
            output.write(loader)
