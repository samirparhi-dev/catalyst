import json
import datetime
import os


def manipulate_snyk_json_file(file_path_snyk):
    print(
        f"ℹ️ Consolidation of snyk report Started")
    try:
        cwe_dictionary = {}
        list_of_cwe_dictionary = []

        with open(file_path_snyk, 'r') as file:
            synk_data = json.load(file)
            list1 = synk_data['runs']
            for index, value in enumerate(list1):
                dict1 = list1[index]
                tool_name = dict1['tool']['driver']['name']
                list2 = dict1['tool']['driver']['rules']
                for dict in list2:
                    code_weakness_description = dict['help']['markdown']
                    cwe = dict['properties']['cwe']
                    severity = dict['properties']['precision']
                    # final_cwe_list.append(cwe)
                    cwe_dictionary['Code Weakness Description'] = code_weakness_description
                    cwe_dictionary['CWE#'] = cwe
                    cwe_dictionary['Severity'] = severity
                    list_of_cwe_dictionary.append(cwe_dictionary)

        return list_of_cwe_dictionary
    except FileNotFoundError:
        print(f"Error: File '{file_path_snyk}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file '{file_path_snyk}'.")


if __name__ == "__main__":
    # Get the user input
    project_name = input("Enter the Project Name:")
    project_language = input("Enter the Project Language:")
    snyk_dictionary = {}
    codeql_dictionary = {}
    sonarqube_dictionary = {}
    timestamp = datetime.datetime.now()
    formatted_timestamp = timestamp.strftime("%Y%m%d%H%M%S")
    final_dict = {}
    final_dict['project'] = project_name
    final_dict['languages'] = project_language
    final_dict['run timestamp'] = formatted_timestamp
    print(
        f"ℹ️ We are about to start Consolidation of snyk report for {project_name}")
    file_path_snyk = input("Enter the path to SnykCode Report  JSON file:")
    snyk_dictionary = manipulate_snyk_json_file(file_path_snyk)
    print(
        f"✅ Consolidation of snyk report for {project_name} Completed Successfully")
    final_dict['Snyk'] = snyk_dictionary
    final_dict['CodeQl'] = codeql_dictionary
    final_dict['SonarQube'] = sonarqube_dictionary

    # Write Json data to a file

    folder_path_to_write = input(
        "Specify the folder path where the Json data will be written. \n\033[1m For example:\033[0m /Users/my_user/test_folder/ :")
    if not os.path.exists(folder_path_to_write):
        os.makedirs(folder_path_to_write)
    file_name = f"Consolidated_static_code_analysis_report_{project_name}_{formatted_timestamp}.json"
    file_path_to_write = folder_path_to_write+file_name

    print(
        f"▶️ Writing consolidated data to {file_path_to_write}")
    with open(file_path_to_write, 'w') as json_file:
        json.dump(final_dict, json_file, indent=4)
    print(
        f"✅ Data Written Successfully to {file_path_to_write}")
