import pandas as pd
import json
import re
import os  
# Define la carpeta donde se encuentran los archivos CSV
carpeta_csv = "csv"

# Define la ruta completa del archivo original
ruta_archivo_original = "usuarios_con_juegos.csv"

# Define la ruta completa del archivo de salida
ruta_archivo_salida = os.path.join(carpeta_csv, "usuarios_juegos.csv")

# Carga el DataFrame desde el archivo original
df_uj = pd.read_csv(ruta_archivo_original)

def separacion_limpieza_juegos(i):
    patron = r'(?<=[a-zA-Z0-9])"(?=[a-zA-Z0-9])'
    
    lista_juegos = df_uj["items"][i]
    lista_juegos = lista_juegos[1:-1].split(sep="}")
    
    for i in range(len(lista_juegos)):
        lista_juegos[i] = lista_juegos[i] + "}"
    
    for i in range(1, len(lista_juegos)):
        lista_juegos[i] = lista_juegos[i][2:]
    
    for i in range(len(lista_juegos)):
        lista_juegos[i] = lista_juegos[i].replace("'", "\"")
        lista_juegos[i] = re.sub(patron, '', lista_juegos[i])
        
    lista_juegos = lista_juegos[:-1]
    
    juegos = []
    for i in range(len(lista_juegos)):
        try:
            json_str = lista_juegos[i]
            juego = json.loads(json_str)
            juegos.append(juego["item_id"] + ";" + juego["item_name"] + ";" 
                          + str(juego["playtime_2weeks"]) + ";" + str(juego["playtime_forever"]))
        except:
            pass
     
    return juegos

juegos = []
lista_procesada = []
for i in range(len(df_uj)):
    df = separacion_limpieza_juegos(i)
    lista_procesada.append(df)

for i in range(len(df_uj)):    
    df_uj["user_id"][i] = str(df_uj["user_id"][i])
    
df_uj["juegos"] = lista_procesada

df_uj.drop("items", axis=1, inplace=True)

# Guarda el DataFrame en un archivo CSV en la carpeta "csv"
df_uj.to_csv(ruta_archivo_salida, index=False)


