# Fonction de recommandation basée sur les codes RIASEC
import pandas as pd
import json

filename = 'Liste des métiers JobIRL_Avec-RIASEC_V2.csv'
df = pd.read_csv(filename, sep = ';', encoding='utf-8')
print(df.head())

def read():
    try:
        df = pd.read_csv(filename, sep = ';', encoding='utf-8')
        #result = df['ROME_PROFESSION_NAME']
        return True
    except Exception as e:
        return False

def reco(RIASEC_majeur, RIASEC_mineur):
    try:
        # filtrer sur RIASEC Majeur (et mineur s'il a été transmis)
        if RIASEC_mineur == '' or RIASEC_mineur == None :
            dfResult = df['Métier'][ df['RIASEC Maj']==RIASEC_majeur ]
        else:
            dfResult = df['Métier'][ (df['RIASEC Maj']==RIASEC_majeur) & (df['RIASEC min']==RIASEC_mineur) ]

        # format json + utf8
        result = json.dumps(dfResult.values.tolist(), ensure_ascii=False)

        print(result)
        return result
        #return True

    except Exception as e:
        print(e)
        return False

