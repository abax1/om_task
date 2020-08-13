import os
from flask import Flask, jsonify, request
from datetime import datetime, time

from src.algorithms.tdsp_dijsktra import tdsp_dijsktra
from src.graph.graph import Graph
from src.io.io import process_input_file

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['JSON_SORT_KEYS'] = False


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

    # Validate the data.
    if start is None:
        return jsonify({
            "message": "start cannot be None.  Please specify a start node e.g. A0"
        }), 400

    if end is None:
        return jsonify({
            "message": "end cannot be None.  Please specify an end node e.g. B2"
        }), 400

    if start_time is None:
        return jsonify({
            "message": "start_time cannot be None.  Please specify a start time e.g. 01:00"
        }), 400

    tmp_file = "tmp_"+file.filename
    file.save(tmp_file)

    graph_data = process_input_file(tmp_file)

    os.remove(tmp_file)

    print("start_time =", start_time.split(':'))
    hour = int(start_time.split(':')[0])
    minute = int(start_time.split(':')[1])

    today = datetime.today()
    t = time(hour, minute)  # input time value
    start_time = datetime(today.year, today.month, today.day, t.hour, t.minute)

    graphs = {}

    for timestep in graph_data:
        # print("Timestep=", timestep)
        # Create a graph for each timestep
        graphs[timestep] = Graph()
        for edge in graph_data.get(timestep):
            graphs[timestep].add_edge(*edge)

    path = tdsp_dijsktra(graphs, start_time, start.upper(), end.upper())

    if path:
        return jsonify({
                "message": "Shortest path successfully calculated.",
                "start": start,
                "end": end,
                "start_time": start_time,
                "path": [node for node in path]
            }), 201
    else:
        return jsonify({
                "message": "Route not possible.",
                "start": start,
                "end": end,
                "start_time": start_time,
                "path": []
            }), 201

