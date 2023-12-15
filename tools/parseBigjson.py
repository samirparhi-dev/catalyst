import ijson


def parse_large_json_file(file_path):
    with open(file_path, 'rb') as f:
        # Use ijson to create an iterator for incremental parsing
        parser = ijson.parse(f)

        # Iterate through the JSON elements
        for prefix, event, value in parser:
            # Process the elements as needed
            print(prefix, event, value)


# Replace 'your_large_file.json' with the path to your actual JSON file
parse_large_json_file(
    '/Users/samir/Documents/code/catalyst/test_folder/hadoop-release-3.3.6-snyk-report.json')
