
import pandas as pd
from random import randrange

df = pd.read_csv('metiers-grands-domaines-et-domaines-professionnels-des-appellations-rome.csv')

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
