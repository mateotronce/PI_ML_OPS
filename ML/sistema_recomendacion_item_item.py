import pandas as pd
import numpy as np

games = pd.read_csv("csv/juegos_limpios.csv")
item_game_matrix = pd.read_csv("csv/matriz_datos_juegos.csv")
user = pd.read_csv("csv/usuarios_juegos.csv")

def recomendacionUserUser(nombre_juego):
    nom_juego = nombre_juego
    nombre_juego = nom_juego
    nombre_juego = nombre_juego.lower()
    games["app_name"] = games["app_name"].str.lower()
    juego = games[games["app_name"] == nombre_juego].index
    id_item = games["id"][games["app_name"] == nombre_juego]
    id_item = id_item.iloc[0]
    juego = juego[0]
    loaded_item_similarity = np.load('ML/item_similarity.npy')
    item_names = item_game_matrix["juego"]
    # Encuentra usuarios similares al usuario objetivo
    similar_items_indices = loaded_item_similarity[item_names[juego]].argsort()[::-1][1:]
    similar_items_indices = similar_items_indices[similar_items_indices != id_item]
       
    print(f"Si te gustan juegos como {nom_juego}, tambien te pueden gustar:")
    num = 0
    i = 0
    while num != 5:
        id_game = int(similar_items_indices[i:i+1][0])
        game = games[games["id"] == id_game]
        try:
            game["id"].iloc[0]
            print(f"Juego:{game['app_name'].iloc[0]} Desarrollador:{game['developer'].iloc[0]}")
            num += 1
            i += 1
        except:
            i += 1
            
recomendacionUserUser("half-life")
