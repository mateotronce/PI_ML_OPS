import pandas as pd
import numpy as np

games = pd.read_csv("csv/juegos_limpios.csv")
user_game_matrix = pd.read_csv("csv/Matriz_Usuarios_Juegos.csv")
user = pd.read_csv("csv/usuarios_juegos.csv")

def recomendacionUserUser(usuario):
    usuario_objetivo = user[user["user_id"] == usuario].index
    usuario_objetivo = usuario_objetivo[0]
    loaded_user_similarity = np.load('user_similarity.npy')
    user_names = user_game_matrix.drop_duplicates(subset=['id_user'])# Debe coincidir con la estructura de tu matriz
    user_names = user_names["id_user"]
    
    # Encuentra usuarios similares al usuario objetivo
    similar_users_indices = loaded_user_similarity[user_names[usuario_objetivo]].argsort()[::-1][1:]
    
    # Genera recomendaciones basadas en juegos de usuarios similares
    user_index = similar_users_indices[usuario_objetivo]
    recomendaciones = []
    juegos_usuario_similar = user_game_matrix[user_game_matrix["id_user"] == user_index]
    for m in range(len(juegos_usuario_similar)):
        if juegos_usuario_similar["horas_juego"].iloc[m] == 0:
            recomendaciones.append(juegos_usuario_similar["id_juego"].iloc[m])
    
    
    print("A usuarios como tu tambien le gustaron:")
    num = 0
    while num != 5: 
        try:
            recomendacion = np.random.choice(recomendaciones, 1, replace=False)
            recomendacion = recomendacion[0]
            juego = games[games["id"] == recomendacion]
            print(f"Titulo:{juego['title'].iloc[0]}  Desarrollador:{juego['developer'].iloc[0]} ")
            num += 1
        except:
            pass
    
recomendacionUserUser("76561197970982479")
