# CS361-Environmental_Log

This microservice project creates an environmental log entry using a Flask framework and REST API. The server runs on the following local port (which can be modified, if needed): http://127.0.0.1:5000/conditions. JSON environmental log entries are stored individually in a directory location called "database/environmental_conditions", which can be modified if needed. There are two (2) paramaters: temperature (in Fahrenheit) and preciptation level. The HTTP methods available to use are POST, GET, and DELETE. DELETE requires input of a log's associated ID.
The user must import json, requests, and os into their code for this microservice to be functional.  

To request data from the microservice, follow this template:
    data = {
        "temperatureF": temperatureInF,
        "precipitation": precipitation,
    }
    data_json = json.dumps(data)
    response = requests.post("http://127.0.0.1:5000/conditions", data_json, headers={'Content-Type': 'application/json'})

To receive data from the microservice, follow this template:
#This reads each individual JSON environmental condition log entry from the directory database/environmental_conditions
    files = os.listdir("database/environmental_conditions")
    for file_name in files:
        file_path = os.path.join("database/environmental_conditions", file_name)
        with open(file_path, "r") as file:
            json_data = json.load(file)
            file_id = os.path.basename(file_name)
            print(f"ID {file_id}:", json_data)
