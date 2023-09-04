from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from tqdm import tqdm
import numpy as np

df_caracteristicas_juegos = pd.read_csv("csv/matriz_datos_juegos.csv")


# Supongamos que df_caracteristicas_juegos es tu DataFrame de características de juegos
similarity_matrix = cosine_similarity(df_caracteristicas_juegos.iloc[:, 1:], df_caracteristicas_juegos.iloc[:, 1:])

np.save('item_similarity.npy', similarity_matrix)
