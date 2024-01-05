import requests

def get_cve_info(cve_id):
    nvd_api_url = f"https://services.nvd.nist.gov/rest/json/cve/{cve_id}"
    
    try:
        response = requests.get(nvd_api_url)
        response.raise_for_status()
        cve_info = response.json()
        return cve_info
    except requests.RequestException as e:
        print(f"Error fetching CVE information: {e}")
        return None

def map_cve_to_owasp_categories(cve_info):
    if cve_info and 'result' in cve_info and 'CVE_Items' in cve_info['result']:
        cve_item = cve_info['result']['CVE_Items'][0]
        
        # Extract relevant information (modify as needed)
        description = cve_item['cve']['description']['description_data'][0]['value']
        cvss_score = cve_item['impact']['baseMetricV2']['cvssV2']['baseScore']

        # Basic mapping based on keywords (modify as needed)
        owasp_categories = {
            'Injection': ['SQL Injection', 'Code Injection', 'Command Injection'],
            'Broken Authentication': ['Authentication Bypass', 'Credential Leak'],
            'Sensitive Data Exposure': ['Information Disclosure', 'Data Exposure'],
            # Add more categories and keywords as needed
        }

        for category, keywords in owasp_categories.items():
            if any(keyword.lower() in description.lower() for keyword in keywords) or cvss_score >= 7.0:
                return category

    return None

def main():
    cve_id = input("Enter CVE ID (e.g., CVE-2022-12345): ")
    cve_info = get_cve_info(cve_id)

    if cve_info:
        owasp_category = map_cve_to_owasp_categories(cve_info)

        if owasp_category:
            print(f"The OWASP category for {cve_id} is: {owasp_category}")
        else:
            print(f"No OWASP category found for {cve_id}")
    else:
        print(f"Failed to fetch CVE information for {cve_id}")

if __name__ == "__main__":
    main()
