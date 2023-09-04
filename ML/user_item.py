from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from tqdm import tqdm
import numpy as np

user_game_matrix = pd.read_csv("csv\Matriz_Usuarios_Juegos.csv")


# Definir una lista de nombres de usuarios que coincida con las filas de la matriz
user_names = user_game_matrix.drop_duplicates(subset=['id_user'])# Debe coincidir con la estructura de tu matriz
user_names = user_names["id_user"]

# Calcula la similitud coseno entre usuarios
# Supongamos que tienes una matriz de usuarios por juegos llamada user_game_matrix
# y deseas dividirla en 10 partes iguales
num_lotes = 1000
tamaño_lote = len(user_game_matrix) // num_lotes

# Inicializa una matriz vacía para almacenar la similitud global
user_similarity_global = None

# Crea una barra de progreso
barra_progreso = tqdm(total=num_lotes, desc="Calculando similitud")

# Calcula la similitud por lotes y combina los resultados
for i in range(num_lotes):
    inicio = i * tamaño_lote
    fin = (i + 1) * tamaño_lote
    user_game_matrix_lote = user_game_matrix[inicio:fin]  # Obtén el lote actual
    
    # Calcula la similitud coseno para el lote actual
    user_similarity_lote = cosine_similarity(user_game_matrix_lote)
    
    if user_similarity_global is None:
        user_similarity_global = user_similarity_lote
    else:
        # Combina los resultados sumando las matrices de similitud
        user_similarity_global += user_similarity_lote
    
    # Actualiza la barra de progreso
    barra_progreso.update(1)

# Cierra la barra de progreso
barra_progreso.close()


# Puedes ordenar las recomendaciones por alguna métrica antes de presentarlas al usuario
np.save('user_similarity.npy', user_similarity_global)

