import pandas as pd
user = pd.read_csv("csv/usuarios_juegos.csv")

usuarios = []
id_juegos = []
horas_juego = []

print("inicio")
num = 0
largo = len(user)
for i in range(len(user)):
    id_u = i
    juegos = user["juegos"][i]
    juegos = juegos.replace("[","").replace("]","").replace(" ","").replace("'","")
    juegos = juegos.split(",")
    for j in range(len(juegos)):
        try:
            juego = juegos[j]
            juego = juego.split(";")
            juego_id = juego[0]
            juego_h = juego[3]
            usuarios.append(id_u)
            id_juegos.append(juego_id)
            horas_juego.append(juego_h)
        except:
            pass
    print(f"termino {num} de {largo}")
    num += 1
    
dic = {"id_user":usuarios,"id_juego":id_juegos,"horas_juego":horas_juego}

df = pd.DataFrame(dic)

df.to_csv("Matriz_Usuarios_Juegos.csv",index=False)
