# JobIRL - Recommandation RIASEC
# Marc@datastrategie -  08/04/2020

import pandas as pd

def read():
    try:

        df = pd.read_csv('metiers-grands-domaines-et-domaines-professionnels-des-appellations-rome.csv', sep = ';', encoding='utf-8')
        #result = df['ROME_PROFESSION_NAME']
        return df

    except Exception as e:
        return False



