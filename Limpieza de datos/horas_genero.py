import pandas as pd

# Cargar los DataFrames de usuarios y juegos
user = pd.read_csv("usuarios_juegos.csv")
games = pd.read_csv("juegos_limpios.csv")

# Extraer la columna "generos" del DataFrame de juegos
categorias = games["generos"]

# Crear una lista para almacenar las categorías de géneros únicas
lista_categorias = []

# Iterar sobre las categorías de géneros y agregar las únicas a la lista
for i in range(len(categorias)):
    opciones = categorias[i].replace(" ", "").replace("[", "").replace("]", "")
    opciones = opciones.split(sep=",")
    for i in range(len(opciones)):
        categoria = opciones[i]
        if categoria not in lista_categorias:
            lista_categorias.append(categoria.replace("'", ""))

# Crear un diccionario para almacenar las horas jugadas por género
horas_juego = [0] * len(lista_categorias)
dic_juegos = dict(zip(lista_categorias, horas_juego))

largo = len(user)
num = 0
print("Iniciando el procesamiento...")

# Iterar sobre los usuarios
for i in range(len(user)):
    user_g = user["juegos"][i].replace(" ", "").replace("[", "").replace("]", "")
    user_g = user_g.split(sep=",")
    
    # Iterar sobre los juegos de cada usuario
    for k in range(len(user_g)):
        try:
            juego = user_g[k].replace("'", "")
            juego = juego.split(sep=";")
            horas_totales = juego[3]
            id_j = juego[0]
            
            # Obtener la lista de géneros del juego a partir del DataFrame de juegos
            lista = games["generos"][games["id"] == int(id_j)].iloc[0].split(",")
            
            # Iterar sobre los géneros del juego y agregar las horas jugadas al diccionario
            for m in range(len(lista)):
                cate = lista[m].replace(" ", "").replace("[", "").replace("]", "").replace("'", "")
                try:
                    dic_juegos[cate] += int(horas_totales)
                except:
                    pass
        except:
            pass
    
    print(f"Procesado {num} de {largo}")
    num += 1

# Crear un DataFrame a partir del diccionario de horas jugadas por género
horas_juego = pd.DataFrame(dic_juegos, index=range(1))

# Guardar el DataFrame en un archivo CSV llamado "horas_genero.csv"
horas_juego.to_csv("horas_genero.csv", index=False)

print("Procesamiento completo. El archivo 'horas_genero.csv' ha sido creado.")
