import pandas as pd

df_costos = pd.read_csv('./data/dfsample/costos.csv')

df_opsales = pd.read_csv('./data/dfsample/opsales.csv')

df_markers = pd.read_csv('./data/dfsample/markers.csv')

# df = pd.read_csv('./data/dfsample/Microempresas_reto_DS4A.csv', delimiter=';', low_memory=False)

# dataset de prueba para el mapa
datatest ={'DEPARTAMENTO': ['SANTANDER', 'ANTIOQUIA', 'CUNDINAMARCA', 'BOYACA'], 
       'COUNT':[99, 900, 9000,900000], 
       'COD_DPTO':['68', '05', '25','15']} 
  
df_maptest = pd.DataFrame.from_dict(datatest)  
