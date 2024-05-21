import json
import os
from flask import Flask, Response, jsonify, request
import uuid

app = Flask(__name__)

@app.route('/conditions', methods=['POST'])
def post_conditions():
    new_conditions = request.json
    temperatureF = new_conditions.get("temperatureF")
    precipitation = new_conditions.get("precipitation")
    
    conditions = {"temperatureF": temperatureF, "precipitation": precipitation}

    conditions_json = json.dumps(conditions)

    filepath = os.path.join("database/environmental_conditions", str(uuid.uuid4()))
    with open(filepath, 'w') as file:
        file.write(conditions_json)
    
    return Response(conditions_json, 200, mimetype='application/json')

@app.route("/conditions", methods=['GET'])
def get_conditions():
    conditions = []
    # Iterate over all files in the directory
    for filename in os.listdir("database/environmental_conditions"):
        # Check if the current file is a regular file (not a directory)
        filepath = os.path.join("database/environmental_conditions", filename)
        if os.path.isfile(filepath):
            with open(filepath, 'r') as file:
                text = file.read()
                condition = json.loads(text)
                condition["id"] = filename
                conditions.append(condition)
    return jsonify(conditions)

@app.route('/conditions/<id>', methods=['DELETE'])
def delete_conditions(id):
    filepath = os.path.join("database/environmental_conditions", id)
    print(filepath)
    if os.path.isfile(filepath):
        os.remove(filepath)
        return Response("", 200, mimetype='application/json')
    else:
        return Response("", 404, mimetype='application/json')

    
