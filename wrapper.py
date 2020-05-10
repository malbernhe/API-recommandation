
import io
import boto3
import pandas as pd
from random import randrange

error=0
bucketname = 'marc-public' # replace with your bucket name
#filename = 'jobirl/rome/grands-domaines-et-domaines-professionnels-des-metiers-rome.csv'
filename = 'jobirl/rome/metiers-grands-domaines-et-domaines-professionnels-des-appellations-rome.csv'

s3 = boto3.client('s3')
obj = s3.get_object(Bucket=bucketname, Key=filename)
try:
    df = pd.read_csv(io.BytesIO(obj['Body'].read()))
except:
    error = 1

def init_data():
    try:
        df = pd.read_csv(io.BytesIO(obj['Body'].read()))
        return True
    except:
        return False



#print (df.head())
#print (df.describe())

def get_data():
    try:
        #result = df['PROFESSIONAL_AREA_NAME'][randrange(100)]
        result = df['ROME_PROFESSION_NAME'][randrange(100)]
        return result
        #return True

    except Exception as e:
        print(e)
        return False



