# Proyecto de Análisis de Datos y Recomendaciones de Juegos en Steam
Este proyecto se centra en el análisis de datos y la generación de recomendaciones de juegos basadas en el comportamiento y las preferencias de los usuarios en la plataforma Steam. Utiliza la biblioteca FastAPI para crear una API web que permite a los usuarios acceder a diferentes tipos de información y recomendaciones relacionadas con los juegos.

# Trabajo Realizado
## Datos Utilizados
El proyecto utiliza varios conjuntos de datos relacionados con Steam y las actividades de los usuarios en la plataforma:

reviews_analisadas.csv: Contiene reseñas de juegos realizadas por los usuarios, incluyendo análisis de sentimientos.
horas_genero.csv: Contiene información sobre las horas jugadas por género de juego.
horas_usuario.csv: Almacena las horas de juego de usuarios específicos.
juegos_limpios.csv: Proporciona información sobre los juegos disponibles en Steam.
Matriz_Usuarios_Juegos.csv: Representa una matriz de usuarios y juegos con información sobre las horas jugadas por cada usuario en cada juego.
usuarios_juegos.csv: Contiene datos de usuarios y la cantidad de juegos que han comprado o adquirido.
matriz_datos_juegos.csv: Contiene información sobre los juegos y su relación con otros juegos (similitud).
Funciones de la API
El proyecto ofrece una serie de funciones de la API que permiten a los usuarios acceder a información y recomendaciones específicas:

/Informacion/{User_id}: Proporciona información sobre un usuario específico, incluyendo la cantidad gastada en juegos y el porcentaje de reseñas positivas realizadas por ese usuario.

/countrev/{fecha_inicio},{fecha_fin}: Calcula el número de reseñas realizadas en un rango de fechas dado y el porcentaje de reseñas positivas en ese período.

/genre/{genero}: Devuelve información sobre un género de juego específico, incluyendo su posición en una lista ordenada y el número total de horas jugadas en ese género.

/usergenre/{genero}: Muestra los 5 jugadores con más horas jugadas en un género de juego específico.

/developer/{publisher}: Ofrece información sobre el número de juegos lanzados por un desarrollador en cada año.

/sentiment/{fecha}: Calcula la cantidad de revisiones con diferentes tipos de sentimiento (negativo, positivo y neutral) en un año específico.

/recomendacionuser/{usuario}: Genera recomendaciones de juegos para un usuario específico basadas en la similitud de comportamiento con otros usuarios.

/recomendacionitem/{item}: Proporciona recomendaciones de juegos similares a uno dado por el nombre del juego.
