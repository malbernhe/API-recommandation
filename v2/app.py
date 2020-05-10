# app.py - a minimal flask api using flask_restful

import wrapper_local as wrapper
from flask import Flask, jsonify
from flask_restful import Resource, Api
import time

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World5"

@app.route('/api/jobirl/list', methods=['GET'])
def list():
    return jsonify(status="ok",
                   result={
                       "nom": "marc",
                       "prenom": "boss"})

@app.route('/api/jobirl/list2', methods=['GET'])
def list2():
    result = wrapper.get_data()
    return jsonify(status="ok",
                   result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


