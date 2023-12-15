import requests

print('~~~The result displayed here fetched from "nvd.nist.gov"~~~')
cwe_id = input("Enter CWE identifier (e.g., 123): ")
base_url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
search_url = f"{base_url}?cweId=CWE-{cwe_id}"
print(f" The API for this action : {search_url}")
try:
    response = requests.get(search_url)
    data = response.json()
    if "vulnerabilities" in data.keys() and len(data['vulnerabilities']) != 0:
        print(f"*********************************************************")
        print(f"{len(data['vulnerabilities'])} CVE(s) found for CWE-{cwe_id}")
        print(f"*********************************************************")
        for vulnerability in data['vulnerabilities']:
            vulnId = vulnerability['cve']['id']
            vulnDes = vulnerability['cve']['descriptions'][0]['value']
            print(f"{vulnId}: {vulnDes}", end="\n\n")
        print(f"*********************************************************")
    else:
        print(f" NO CVE related to CWE-{cwe_id} found in `nvd.nist.gov` DB")
    # return []
except Exception as e:
    print(f"Error: {e}")
