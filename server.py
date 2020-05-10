#
# API serveur Flask
#

#import wrapper as wrapper
import wrapper_local as wrapper

from flask import Flask, jsonify, request
import time

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/api/jobirl/list2', methods=['GET'])
def list2():
    tic = time.perf_counter()
    result = wrapper.get_data()
    toc = time.perf_counter()
    #print(result)
    #print(f"Get data in {toc - tic:0.4f} seconds")
    return jsonify(status="ok",
                   result=result)


@app.route('/api/jobirl/list', methods=['GET'])
def list():
    return jsonify(status="ok",
                   result={
                       "nom": "marc",
                       "prenom": "boss"})

    # result = wrapper.get_all_users()
    # if result:
    #     return jsonify(status="True",
    #     result= [
    #         {"nom":user.nom,
    #          "prenom":user.prenom,
    #          "email":user.email,
    #          "ville": user.ville,
    #          "telephone": user.telephone} for user in result.all() ])
    # return jsonify(status="False")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)