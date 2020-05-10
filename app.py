# app.py - flask api using flask_restful
#
# http://localhost:5000/api/jobirl/reco?majeur=I
# http://localhost:5000/api/jobirl/reco?majeur=C

#import wrapper_local as wrapper
import wrapper as wrapper
import recommand
from flask import Flask, request, jsonify
#from flask_restful import Resource, Api
import time

RIASEC_majeur = ''
RIASEC_mineur = ''

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

@app.route('/api/jobirl/init', methods=['GET'])
def init():
    result = wrapper.init_data()
    return jsonify(status="ok",
                   result=result)


@app.route('/api/jobirl/list2', methods=['GET'])
def list2():
    result = wrapper.get_data()
    return jsonify(status="ok",
                   result=result)

@app.route('/api/jobirl/reco', methods=['GET'])
def reco():
    RIASEC_majeur = request.args.get('majeur')
    RIASEC_mineur = request.args.get('mineur')

    result = recommand.reco(RIASEC_majeur, RIASEC_mineur)

    return result
#    return jsonify(result)
#    return jsonify(status="ok",
#                   result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


