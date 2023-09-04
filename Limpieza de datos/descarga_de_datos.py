import json
import ast
import pandas as pd

def descargaJson(camino,nombre_descarga):
    rows = []
    with open(camino, encoding="MacRoman") as f:
      for line in f.readlines():
          rows.append(ast.literal_eval(line))
    df = pd.DataFrame(rows)
    df.to_csv(nombre_descarga,index=False)
    
def descargaGames(camino,nombre_descarga): 
    df = pd.read_json(camino,lines=True)
    df.to_csv(nombre_descarga,index=False)
      

