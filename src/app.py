import os

from flask import Flask, jsonify, request
from flask_restful import reqparse, Api
from datetime import datetime

from src.io.io import process_input_file

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/ping', methods=['GET'])
def hello():
    return jsonify({
        "message": "Hello world, from Dijkstra!",
        "local_time": "{}".format(datetime.now())
    }), 200


@app.route('/route', methods=['POST'])
def route():
    file = request.files['file']
    start = request.args.get('start', default=None, type=str)
    end = request.args.get('end', default=None, type=str)
    start_time = request.args.get('start_time', default=None, type=str)

    print(start)

    file_extension = file.filename[-4:]
    tmp_file = "tmp_"+file.filename
    file.save(tmp_file)

    graphs = process_input_file(tmp_file)

    os.remove(tmp_file)

    print(graphs[0])

    return jsonify({
            "message": "Hello world, from Dijkstra!",
            "start": start,
            "end": end,
            "start_time": start_time,
            "file_extension": "{}".format(file_extension)
        }), 201
