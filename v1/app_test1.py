# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask_restful import Resource, Api

import boto3
import pandas as pd
import io
from random import randrange


print("Debut")

bucketname = 'marc-public' # replace with your bucket name
#filename = 'jobirl/rome/grands-domaines-et-domaines-professionnels-des-metiers-rome.csv'
filename = 'jobirl/rome/metiers-grands-domaines-et-domaines-professionnels-des-appellations-rome.csv'

s3 = boto3.client('s3')

obj = s3.get_object(Bucket=bucketname, Key=filename)
df = pd.read_csv(io.BytesIO(obj['Body'].read()))

result = df['ROME_PROFESSION_NAME'][randrange(100)]
print(result)


app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return result

@app.route('/api/jobirl/list2', methods=['GET'])
def list2():
    tic = time.perf_counter()
    result = wrapper.get_data()
    toc = time.perf_counter()
    #print(result)
    #print(f"Get data in {toc - tic:0.4f} seconds")
    return jsonify(status="ok",
                   result=str(result))


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


