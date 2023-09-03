import pandas as pd
import numpy as np
from datetime import datetime
import ast

re = pd.read_csv("csv/reviews_analisadas.csv")
horas_juego = pd.read_csv("csv/horas_genero.csv")
u_h = pd.read_csv("csv/horas_usuario.csv")
games = pd.read_csv("csv/juegos_limpios.csv")
user_game_matrix = pd.read_csv("csv/Matriz_Usuarios_Juegos.csv")
user = pd.read_csv("csv/usuarios_juegos.csv")
item_game_matrix = pd.read_csv("csv/matriz_datos_juegos.csv")

def userdata(User_id):
    # Función para calcular la cantidad gastada por un usuario
    def cantidadGastada(User_id):
        # Busca al usuario con el ID proporcionado en un DataFrame llamado 'user'
        usuario = user[user["user_id"] == str(User_id)]
        
        # Extrae información sobre los juegos y la cantidad de ítems que ha comprado el usuario
        juegos = usuario["juegos"].iloc[0]
        cantidad_item = usuario["items_count"].iloc[0]
        
        # Procesa la lista de juegos comprados por el usuario
        lista_juegos = juegos[1:-1]
        lista_juegos = lista_juegos.split(sep=",")
        
        # Inicializa listas para almacenar los IDs de juegos y sus precios
        lista_id = []
        lista_precio = []
        
        # Procesa cada juego en la lista de juegos
        for i in range(1, len(lista_juegos)):
            lista_juegos[i] = lista_juegos[i][1:]
            datos = lista_juegos[i].split(sep=";")
            id_g = datos[0][1:]
            lista_id.append(id_g)
        
        # Filtra los IDs que son numéricos
        lista_id = [item for item in lista_id if item.isnumeric()]
        
        # Obtiene los precios de los juegos y los agrega a la lista de precios
        for k in range(len(lista_id)):
            try:
                precio = games["price"][games["id"] == int(lista_id[k])]
                precio = precio.iloc[0]
                lista_precio.append(precio)
            except:
                pass
        
        # Convierte los precios a números flotantes
        precios_verdad = []
        for n in range(len(lista_precio)):
            try:
                lista_precio[n] = float(lista_precio[n])
                precios_verdad.append(lista_precio[n])
            except:
                pass
        
        # Calcula la suma de los precios y redondea a 2 decimales
        suma = round(sum(precios_verdad), 2)
        
        return suma, cantidad_item
    
    # Función para obtener el porcentaje de reseñas positivas de un usuario
    def reviewsUsuario(User_id):
        lista = []
        verdadero = 0
        
        try:
            # Busca al usuario con el ID proporcionado en un DataFrame llamado 're'
            usuario = re[re["user_id"] == str(User_id)]
            reviews = usuario["Analisis"].iloc[0]
            reviews = reviews.split(sep=";")
            
            cantidad = 0
            
            # Procesa las reseñas del usuario
            for i in range(2, len(reviews), 3):
                lista.append(reviews[i])
                if reviews[i] == "True":
                    verdadero += 1
                cantidad += 1
                
            # Calcula el porcentaje de reseñas positivas
            porcentaje = str((round(verdadero / cantidad, 2)) * 100) + "%"
    
            return porcentaje, cantidad
        except:
            porcentaje = cantidad = "No tiene reseñas"
            return porcentaje, cantidad
    
    # Llama a las funciones para obtener la cantidad gastada y el porcentaje de reseñas
    plata_gastada, items = cantidadGastada(User_id)
    porcentaje, cantidad = reviewsUsuario(User_id)
    
    # Comprueba las condiciones y devuelve un mensaje apropiado
    if items == 0:
        return print(f"El usuario {User_id} no tiene ningún juego")
    elif porcentaje != "No tiene reseñas":
        return print(f"El usuario {User_id} gastó {plata_gastada}$ en {items} juegos," +
                     f" también realizó {cantidad} reviews recomendando en un {porcentaje} de estas")
    else:
        return print(f"El usuario {User_id} gastó {plata_gastada}$ en {items} juegos y no tiene reseñas")
   
    
userdata("doctr")


def countreviews(fecha_inicio, fecha_fin):
    # Convierte las fechas de inicio y fin en objetos datetime
    fecha_inicio_obj = datetime.strptime(fecha_inicio, "%Y-%m-%d")
    fecha_fin_obj = datetime.strptime(fecha_fin, "%Y-%m-%d")
    
    # Calcula la diferencia en días entre las dos fechas
    diferencia = fecha_fin_obj - fecha_inicio_obj
    diferencia_en_dias = diferencia.days
    
    # Obtiene las columnas de reseñas y user_id del DataFrame 're'
    revis = re["Analisis"]
    user = re["user_id"]
    
    # Inicializa listas para almacenar fechas, reseñas y user_id en un formato más manejable
    lista_fechas = []
    fechas_en_rango = []
    positivo = 0
    total = 0
    
    # Itera sobre las reseñas
    for i in range(len(revis)):
        reviews = revis[i].replace("[", "").replace("]", "")
        reviews = reviews.split(sep=",")
        for review in reviews:
            valores = review.split(sep=";")
            try:
                lista_fechas.append((valores[1], valores[2], user[i]))
            except:
                pass
    
    # Filtra las fechas en el rango especificado
    for fecha in lista_fechas:
        if fecha_inicio_obj <= datetime.strptime(fecha[0], "%Y-%m-%d") <= fecha_fin_obj:
            fechas_en_rango.append(fecha)
    
    # Calcula el número de reseñas positivas y totales
    for i in range(len(fechas_en_rango)):
        if fechas_en_rango[i][1] == "True":
            positivo += 1
        total += 1
    
    # Calcula la cantidad de usuarios únicos que hicieron reseñas en el rango de fechas
    cantidad = len(fechas_en_rango)
    
    if total != 0:
        # Calcula el porcentaje de reseñas positivas
        porcentaje = round((positivo / total) * 100, 2)
        
        # Calcula el número de usuarios únicos
        usuarios = len(np.unique([fecha[2] for fecha in fechas_en_rango]))
        
        return print(f"{usuarios} usuarios hicieron {cantidad} reviews, con un {porcentaje}% de reseñas positivas en un periodo de {diferencia_en_dias} días")
    else:
        return print("No hubo comentarios")

    
countreviews("2015-07-15","2016-07-15")


def genre(genero):
    # Obtiene el orden de las columnas en el DataFrame 'horas_juego' en orden descendente
    column_order = horas_juego.iloc[0].sort_values(ascending=False).index
    
    # Obtiene la posición del género especificado en base 1 en el orden de las columnas
    posicion = column_order.get_loc(genero) + 1  
    
    # Obtiene la cantidad de horas asociadas al género especificado
    horas = horas_juego[genero].iloc[0]
    
    # Imprime la información sobre la posición y las horas del género
    print(f"La columna '{genero}' está en la posición {posicion} con {horas} horas en total.")
  
genre("Action")

def userforgenre(genero):
    # Inicializa una lista para almacenar las horas totales de cada usuario en el género especificado
    horas_tot = []

    # Itera sobre las filas del DataFrame 'u_h'
    for i in range(len(u_h)):
        usuario = u_h.iloc[i]
        data_str = usuario[2]
        
        # Convierte la cadena de datos en un diccionario
        data_dict = ast.literal_eval(data_str)
        
        # Obtiene las horas jugadas en el género especificado
        horas_g = data_dict[genero]
        
        # Agrega las horas totales a la lista
        horas_tot.append(horas_g)

    # Agrega una columna 'horas' al DataFrame 'u_h' con las horas totales
    u_h["horas"] = horas_tot
    
    # Ordena el DataFrame por horas en orden descendente
    sorted_df = u_h.sort_values(by='horas', ascending=False)
    
    # Obtiene los 5 usuarios con más horas en el género especificado
    top_5 = sorted_df[["0", "horas", "user_url"]].head(5)
    
    # Imprime el encabezado
    print(f"Los 5 jugadores con más horas en {genero} son:")
    print("puesto| usuario             | horas   | url_user")
    print("-" * 50)
    
    num = 1
    va = 0

    # Imprime los 5 mejores usuarios con formato
    for i in range(len(top_5)):
        usuario = top_5['0'].iloc[va]
        horas = top_5['horas'].iloc[va]
        url_user = top_5['user_url'].iloc[va]
    
        # Ajustamos los números de ancho para lograr la alineación
        print(f"{num:<6}| {usuario:<20}| {horas:<8}| {url_user}")
        
        num += 1
        va += 1

userforgenre("Indie")

def developer(publisher):
    # Inicializa una lista para almacenar los años de lanzamiento únicos
    lista_fechas = []

    # Itera sobre los juegos en el DataFrame 'games'
    for i in range(len(games)):
        fecha = games["release_date"].iloc[i]
        fecha = fecha.split("-")  # Divide la fecha en partes usando "-"
        fecha = fecha[0]  # Toma el primer elemento (año)

        # Manejo especial para fechas como "Jul 2010" (toma los últimos 4 caracteres)
        try:
            int(fecha)
        except:
            fecha = fecha[-4:]
        
        # Elimina comillas simples si están presentes
        fecha = fecha.replace("'", "")

        # Agrega el año a la lista de años si aún no está presente
        if fecha not in lista_fechas:
            lista_fechas.append(fecha)
    
    # Ordena la lista de años
    lista_fechas.sort()   
    empresa = []

    # Itera sobre los años y realiza cálculos relacionados con el desarrollador
    for fecha in lista_fechas:
        dev = games[games["developer"] == publisher]
        dev = dev[dev["release_date"].str[0:4] == fecha]
        gratis = 0
        total = 0
        
        # Itera sobre los juegos del desarrollador en el año actual
        for i in dev.index:
            juego = dev[dev.index == i]
            precio = juego["price"].iloc[0]
            fecha_salida = juego["release_date"]
            
            try:
                precio = float(precio)
                total += 1
            except:
                total += 1
                gratis += 1
        
        # Agrega información sobre el año, cantidad total de juegos y cantidad de juegos gratis
        empresa.append(fecha + ";" + str(total) + ";" + str(gratis))
    
    # Imprime la información sobre juegos y contenido gratuito por año
    porcen = []
    print("Año     | Juegos | Contenido gratis")
    print("-" * 30)  # Línea de separación

    for año in empresa:
        año = año.split(sep=";")
        if año[1] != "0":    
            porcentaje = round((int(año[2]) / int(año[1])) * 100)
            print(f"{año[0]: <8} | {año[1]: <7} | {porcentaje}%")


developer("Capcom")

def sentiment_analysis(fecha):
    r = []
    rev = re["Analisis"]
    
    # Itera sobre las revisiones en el DataFrame 're'
    for j in range(len(rev)):
        review = rev[j]
        review = review.replace("[", "").replace("]", "").replace("'", "").replace(" ", "")
        review = review.split(",")
        
        # Itera sobre los elementos de cada revisión
        for k in range(len(review)):
            try:
                tw = review[k].split(";")
                fecha_r = int(tw[1][:4])  # Obtiene el año de la revisión
                
                # Si la fecha coincide con el año proporcionado
                if fecha == fecha_r:
                    r.append(tw[3])  # Agrega el sentimiento (0, 1 o 2) a la lista 'r'
            except:
                pass

    # Inicializa contadores para cada tipo de sentimiento
    contador_0 = 0
    contador_1 = 0
    contador_2 = 0
    total = 0
    
    # Itera sobre la lista 'r' para contar la cantidad de cada tipo de sentimiento
    for elemento in r:
        if elemento == "0":
            contador_0 += 1
        elif elemento == "1":
            contador_1 += 1
        elif elemento == "2":
            contador_2 += 1    
        total += 1
    
    # Imprime la cantidad de revisiones con cada tipo de sentimiento
    print(f"La cantidad es [Negativos:{contador_0}, Positivos:{contador_2}, Neutros:{contador_1}]")
    
sentiment_analysis(2015)

def recomendacionUseritem(usuario):
    usuario_objetivo = user[user["user_id"] == usuario].index
    usuario_objetivo = usuario_objetivo[0]
    loaded_user_similarity = np.load('ML/user_similarity.npy')
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
    
    #Devuelve las recomendaciones
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
    
recomendacionUseritem("76561197970982479")

def recomendacionitemitem(nombre_juego):
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
            
recomendacionitemitem("half-life")

