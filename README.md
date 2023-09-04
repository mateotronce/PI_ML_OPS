# Proyecto de Análisis de Datos y Recomendaciones de Juegos en Steam
Este proyecto se centra en el análisis de datos y la generación de recomendaciones de juegos basadas en el comportamiento y las preferencias de los usuarios en la plataforma Steam. Utiliza la biblioteca FastAPI para crear una API web que permite a los usuarios acceder a diferentes tipos de información y recomendaciones relacionadas con los juegos.

## Datos Utilizados
El dataset utilizado se encuentra en: [Enlace al dataset](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj).

# Trabajo Realizado
El proyecto utiliza varios conjuntos de datos relacionados con Steam y las actividades de los usuarios en la plataforma. Los datos se obtuvieron en formato JSON, por lo que se transformaron a formato CSV para un mejor tratamiento de estos. A partir de esto, se generaron distintos archivos CSV para facilitar el ingreso de los datos a la API. Por ejemplo, en el dataset de juegos, se eliminaron los archivos nulos que venían en el JSON. Luego, se realizaron las funciones que se utilizarán en la API y, utilizando un modelo de similitud coseno, se generó una matriz de correlaciones entre usuarios y otra de ítems. A partir de esto, se generaron las últimas dos funciones de predicción.

## ¿Qué archivos se utilizan dentro de la API?

Se utilizan los siguientes archivos:

- `reviews_analizadas.csv`: Contiene reseñas de juegos realizadas por los usuarios, incluyendo análisis de sentimientos.
- `horas_genero.csv`: Contiene información sobre las horas jugadas por género de juego.
- `horas_usuario.csv`: Almacena las horas de juego de usuarios específicos.
- `juegos_limpios.csv`: Proporciona información sobre los juegos disponibles en Steam.
- `Matriz_Usuarios_Juegos.csv`: Representa una matriz de usuarios y juegos con información sobre las horas jugadas por cada usuario en cada juego.
- `usuarios_juegos.csv`: Contiene datos de usuarios y la cantidad de juegos que han comprado o adquirido.
- `matriz_datos_juegos.csv`: Contiene información sobre los juegos y su relación con otros juegos (similitud).

## Funciones de la API

El proyecto ofrece una serie de funciones de la API que permiten a los usuarios acceder a información y recomendaciones específicas:

- `/Informacion/{User_id}`: Proporciona información sobre un usuario específico, incluyendo la cantidad gastada en juegos y el porcentaje de reseñas positivas realizadas por ese usuario.
- `/countrev/{fecha_inicio},{fecha_fin}`: Calcula el número de reseñas realizadas en un rango de fechas dado y el porcentaje de reseñas positivas en ese período.
- `/genre/{genero}`: Devuelve información sobre un género de juego específico, incluyendo su posición en una lista ordenada y el número total de horas jugadas en ese género.
- `/usergenre/{genero}`: Muestra los 5 jugadores con más horas jugadas en un género de juego específico.
- `/developer/{publisher}`: Ofrece información sobre el número de juegos lanzados por un desarrollador en cada año.
- `/sentiment/{fecha}`: Calcula la cantidad de revisiones con diferentes tipos de sentimiento (negativo, positivo y neutral) en un año específico.

### Funciones de Machine Learning en la API

- `/recomendacionuser/{usuario}`: Genera recomendaciones de juegos para un usuario específico basadas en la similitud de comportamiento con otros usuarios.
- `/recomendacionitem/{item}`: Proporciona recomendaciones de juegos similares a uno dado por el nombre del juego.
- 
## ¿Qué hay en las carpetas?

Hay tres carpetas en total. Dentro de la carpeta "csv", se encuentran todos los archivos de tipo CSV que se utilizan para la toma de información. En la carpeta "ML" se encuentra el trabajo que se realizó con los datos para que pudieran ser utilizados con el modelo. También se encuentran los archivos de NumPy que sirven como base para las relaciones entre los usuarios y los elementos. Por último, está la carpeta de "Limpieza de datos", que como su nombre indica, contiene los códigos que se utilizaron en el proceso ETL, los cuales se aplicaron a los archivos mencionados en la sección de "datos utilizados".

## ¿Y los archivos que no están en carpetas?

estos son los siguientes:

1. **README**: Este es el archivo que estás leyendo en este momento.
2. **app.py**: Aquí se encuentra desarrollada la API, por lo que las funciones de la API se toman de este archivo.
3. **funciones_API.py**: Estas son las mismas funciones de la API, pero están diseñadas para ejecutarse de manera local sin la necesidad de la librería FastAPI.
4. **requirements.txt**: Este archivo contiene la lista de dependencias que tu máquina necesita para ejecutar todos los archivos sin problemas. Para instalar estas dependencias, debes usar el siguiente comando:

```bash
pip install -r requirements.txt
