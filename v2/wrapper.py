
#import io
import boto3
import pandas as pd
from random import randrange

bucketname = 'marc-public' # replace with your bucket name
#filename = 'jobirl/rome/grands-domaines-et-domaines-professionnels-des-metiers-rome.csv'
filename = 'jobirl/rome/metiers-grands-domaines-et-domaines-professionnels-des-appellations-rome.csv'

s3 = boto3.client('s3')

#obj = s3.get_object(Bucket=bucketname, Key=filename)
#df = pd.read_csv(io.BytesIO(obj['Body'].read()))


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
        return e



