import sys
import requests
from bs4 import BeautifulSoup
import json

bold_text = "\033[1m"
reset_format = "\033[0m"
line_separator = '*' * 30
output_data = []
output_format = "json"


def fetch_cwe_details(cwe_id):
    url = f"https://cwe.mitre.org/data/definitions/{cwe_id}.html"
    response = requests.get(url)
    # print(response)
    if response.status_code == 200:
        html_content = response.text
        # print(html_content)
        soup = BeautifulSoup(response.text, 'html.parser')
        if soup:
            h2_element = soup.find('h2')

            if h2_element:
                issueType = h2_element.text.strip()
                # print(f"{bold_text}Issue Type :{reset_format}", issueType)

            else:
                print(f"No Issue Type found for {cwe_id}")

            description_div = soup.find('div', {'id': 'Description'})
            if description_div:
                detail_div = description_div.find('div', {'class': 'detail'})
            else:
                print(f"No Description found for {cwe_id}")
            if detail_div:
                description_text = detail_div.get_text(strip=True)
                # print(f"{bold_text}\nDescription : {reset_format}",
                #       description_text)
            else:
                print(f"No Description Detail found for {cwe_id}")

            extensive_description_div = soup.find(
                'div', {'id': 'Extended_Description'})
            if extensive_description_div:
                detail_extensive_description_div = extensive_description_div.find('div', {
                                                                                  'class': 'detail'})
            else:
                print(f"No Extended Description found for {cwe_id}")

            if detail_extensive_description_div:
                detail_extensive_description_text = detail_extensive_description_div.get_text(
                    strip=True)
                # print(f"{bold_text}\nDetailed Description : {reset_format}",
                #       detail_extensive_description_text)
                # print(line_separator)
            else:
                print(f"No Extended Description found for {cwe_id}")
                print(line_separator)
    else:
        print(f"There is somthing wrong with {cwe_id} Kindly have a look")
    # if output_format == "json":
    dict = {
        "Issue Type": issueType,
        "Description": description_text,
        "Detailed Description": detail_extensive_description_text
    }
    return dict

    if response.status_code != 200:
        print(f"Failed to fetch CWE details for {cwe_id}")
        return


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cwe_details.py <CWE-IDs separated by spaces>")
        print(line_separator)
        sys.exit(1)

    cwe_ids = sys.argv[1:]

    for cwe_id in cwe_ids:
        parts = cwe_id.split("-")
        cwe_number = parts[1]
        input_dict = fetch_cwe_details(cwe_number)
        output_data.append(input_dict)
json_output = json.dumps(output_data, indent=4)
print(json_output)
