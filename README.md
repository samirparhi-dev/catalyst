# catalyst
- The motive of this Repository to develop script that are intended to use in github action / any kind of server-less application setup.

- Scripts here are not specific to any technology or segment. You can develop any small script to become more productive at work.
- People are encourage to Contribute even small script and we aim this space to be the goto place for all system engineers/beginners/Cyber security practitioner/student/any one who is interested to learn.

## How to ?

- `tools` directory contains all the script that can be reused and consumed for various purpose. Usage of this script are very simple and acts as accelerators to improve some ones productivity.

- `vars` folder contains jenkins pipeline groovy script for reference to get an idea how to write Shared library based pipeline in jenkins

- `docker` Directory contains Dockerfile/Docker compose file/anything related to docker.

- `test_folder` contains all the sample files which can be used along with the script to validate the intended output.

## Explanation of Each scripts:

- `tools/blobsign-cosign.sh` : To sign a file / SBOM / any blob using the sigstore's Cosign utility.
- `tools/cwe_details.py` : The python script to scarp CWE details from CWE sites
- `tools/cweCveAssociation.py` : This Script finds all the possible CVE for given CWEs.
- `tools/parseBigjson.py` : WIP
- `tools/Static_code_analysis_consolidation_report.py` : This script is quiet interesting , It processes all the static code analysis files that are obtained as json format from `Snyk` `CodeQl` and `SonarQube` and creates a consolidated Json file which can be further processed for various purpose, For example 
    1. To reduce the false positive
    2. Prioritize the issue to be fixed
    3. Remove anomalies etc.
