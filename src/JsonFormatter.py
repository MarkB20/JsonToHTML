import json
import os
import textwrap  # Add this line to import the textwrap module

def JsonFormatter(input_path):
    for file in os.listdir(input_path):
        json_file_path = os.path.join(input_path, file)

        # Skip non-JSON files
        if not file.endswith('.json'):
            continue

        with open(json_file_path) as f:
            try:
                loader = json.load(f)
            except json.JSONDecodeError as e:
                print(f"Error loading JSON from {json_file_path}: {e}")
                continue  # Skip to the next file if loading fails

        # Process the JSON data
        for meal in loader.get("meals", []):
            # Ensure 'strinstructions' is present and not empty
            if "strinstructions" in meal and meal["strinstructions"]:
                # Assuming a fixed table width of 80 characters
                formatted_instructions = textwrap.fill(
                    meal["strinstructions"], width=80, initial_indent="    ", subsequent_indent="    "
                )
                meal["strinstructions"] = formatted_instructions

        # Save the modified JSON back to the output directory
        output_directory = "outputJSONFile"
        output_file_path = os.path.join(output_directory, file)
        with open(output_file_path, 'w') as output:
            json.dump(loader, output, indent=4)
