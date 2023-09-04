import pandas as pd

# Carga de los DataFrames
user = pd.read_csv("usuarios_juegos.csv")
games = pd.read_csv("juegos_limpios.csv")
re = pd.read_csv("reviews_analisadas.csv")

# Lista de categorías de géneros de juegos
categorias = games["generos"]
lista_categorias = []

# Itera sobre las categorías de géneros para construir la lista de categorías
for categoria_string in categorias:
    opciones = categoria_string.replace(" ", "").replace("[", "").replace("]", "")
    opciones = opciones.split(sep=",")
    
    for categoria in opciones:
        categoria = categoria.replace("'", "")
        if categoria not in lista_categorias:
            lista_categorias.append(categoria)

# Lista para almacenar las horas jugadas por género para cada usuario
lista_user_horas = []
print("Inicia el procesamiento...")
largo = len(user)
num = 0

# Itera sobre los usuarios
for i in range(len(user)):
    horas_juego = [0] * len(lista_categorias)
    dic_juegos = dict(zip(lista_categorias, horas_juego))
    
    usuario_juegos = user["juegos"].iloc[i]
    usuario_juegos = usuario_juegos.replace("[", "").replace("]", "").replace("'", "")
    juegos = usuario_juegos.split(sep=",")
    
    # Itera sobre los juegos del usuario
    for juego in juegos:
        try:
            juego_info = juego.split(sep=";")
            horas_totales = juego_info[3]
            id_j = juego_info[0]
            categorias_juego = games["generos"][games["id"] == int(id_j)].iloc[0].split(",")

            # Asigna las horas jugadas del juego a las categorías correspondientes
            for categoria in categorias_juego:
                categoria = categoria.replace(" ", "").replace("[", "").replace("]", "").replace("'", "")

                try:
                    dic_juegos[categoria] += int(horas_totales)
                except:
                    pass
        except:
            pass

    # Agrega la información del usuario y sus horas jugadas por género a la lista
    lista_user_horas.append((user["user_id"].iloc[i], dic_juegos))
    print(f"Procesado {num} de {largo}")
    num += 1

# Crea un DataFrame a partir de la lista de horas jugadas por género
indi = range(len(lista_user_horas))
lista = pd.DataFrame(lista_user_horas, index=indi)

# Agrega la columna 'user_url' al DataFrame
lista["user_url"] = user["user_url"]

# Guarda el DataFrame en un archivo CSV llamado "horas_usuario.csv"
lista.to_csv("horas_usuario.csv", index=False)
print("Procesamiento completo. El archivo 'horas_usuario.csv' ha sido creado.")
