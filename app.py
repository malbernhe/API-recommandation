# JobIRL - Recommandation RIASEC
# flask api using flask_restful - Marc@datastrategie -  08/04/2020

# http://localhost:5000/api/jobirl/reco?majeur=I
# http://localhost:5000/api/jobirl/reco?majeur=I&mineur=C

#import wrapper_local as wrapper
#import wrapper as wrapper
import recommand
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
@app.route('/api/jobirl/info')
def index():
    return "API JobIRL - Recommandation RIASEC"

@app.route('/api/jobirl/read', methods=['GET'])
def read():
    df = recommand.read()
    return jsonify(status="ok",
                   result=df)

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


