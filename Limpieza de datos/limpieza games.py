import pandas as pd

# Carga el DataFrame desde el archivo "juegos.csv"
df_j = pd.read_csv("juegos.csv")

# Elimina filas con valores NaN (valores faltantes)
df_j.dropna(inplace=True)

# Inicializa una lista para almacenar los géneros limpios
generos = []

# Itera sobre las filas del DataFrame
for i in range(len(df_j["genres"])):
    gener_j = df_j["genres"][i:i+1]
    gener_j = gener_j.tolist()
    gener_j = gener_j[0].split(sep=",")
    
    # Procesa cada género en la lista
    for j in range(len(gener_j)):
        gener_j[j] = gener_j[j].replace("[", "")
        gener_j[j] = gener_j[j].replace("]", "")
        gener_j[j] = gener_j[j].replace("'", "")
    
    # Agrega la lista de géneros limpios a la lista 'generos'
    generos.append(gener_j)

# Agrega una nueva columna 'generos' al DataFrame original
df_j["generos"] = generos

# Elimina la columna original 'genres' del DataFrame
df_j.drop("genres", axis=1, inplace=True)

# Crea un nuevo DataFrame 'df_idg' con las columnas 'id' y 'generos'
df_idg = df_j[["id", "generos"]]

# Guarda el DataFrame 'df_j' en un archivo CSV llamado "juegos_limpios.csv"
df_j.to_csv("juegos_limpios.csv", index=False)

# Guarda el DataFrame 'df_idg' en un archivo CSV llamado "id_genero.csv"
df_idg.to_csv("id_genero.csv", index=False)
