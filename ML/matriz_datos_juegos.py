import pandas as pd

ju  = pd.read_csv("csv/juegos_limpios.csv")

juego = []
Action = []
Casual = []
Indie = []
Simulation = []
Strategy = []
FreetoPlay = []
RPG = []
Sports = []
Adventure = []
Racing = []
EarlyAccess = []
MassivelyMultiplayer = []
AnimationModeling = []
WebPublishing = []
Education = []
SoftwareTraining = []
Utilities = []
DesignIllustration = []
AudioProduction = []
VideoProduction = []
PhotoEditing = []

for i in range(len(ju)):
    contador_Action = 0
    contador_Casual = 0
    contador_Indie = 0
    contador_Simulation = 0
    contador_Strategy = 0
    contador_FreetoPlay = 0
    contador_RPG = 0
    contador_Sports = 0
    contador_Adventure = 0
    contador_Racing = 0
    contador_EarlyAccess = 0
    contador_MassivelyMultiplayer = 0
    contador_AnimationModeling = 0
    contador_WebPublishing = 0
    contador_Education = 0
    contador_SoftwareTraining = 0
    contador_Utilities = 0
    contador_DesignIllustration = 0
    contador_AudioProduction = 0
    contador_VideoProduction = 0
    contador_PhotoEditing = 0

    juego_id = int(ju["id"][i])
    juego_generos = ju["generos"][i].replace("[","").replace("]","").replace(" ","").replace("'","")
    generos = juego_generos.split(",")
    for genero in generos:
        if genero == "Action":
            contador_Action += 1
        elif genero == "Casual":
            contador_Casual += 1
        elif genero == "Indie":
            contador_Indie += 1
        elif genero == "Simulation":
            contador_Simulation += 1
        elif genero == "Strategy":
            contador_Strategy += 1
        elif genero == "FreetoPlay":
            contador_FreetoPlay += 1
        elif genero == "RPG":
            contador_RPG += 1
        elif genero == "Sports":
            contador_Sports += 1
        elif genero == "Adventure":
            contador_Adventure += 1
        elif genero == "Racing":
            contador_Racing += 1
        elif genero == "EarlyAccess":
            contador_EarlyAccess += 1
        elif genero == "MassivelyMultiplayer":
            contador_MassivelyMultiplayer += 1
        elif genero == "Animation&Modeling":
            contador_AnimationModeling += 1
        elif genero == "WebPublishing":
            contador_WebPublishing += 1
        elif genero == "Education":
            contador_Education += 1
        elif genero == "SoftwareTraining":
            contador_SoftwareTraining += 1
        elif genero == "Utilities":
            contador_Utilities += 1
        elif genero == "Design&Illustration":
            contador_DesignIllustration += 1
        elif genero == "AudioProduction":
            contador_AudioProduction += 1
        elif genero == "VideoProduction":
            contador_VideoProduction += 1
        elif genero == "PhotoEditing":
            contador_PhotoEditing += 1
    juego.append(juego_id)        
    Action.append(contador_Action)
    Casual.append(contador_Casual)
    Indie.append(contador_Indie)
    Simulation.append(contador_Simulation)
    Strategy.append(contador_Strategy)
    FreetoPlay.append(contador_FreetoPlay) 
    RPG.append(contador_RPG)
    Sports.append(contador_Sports) 
    Adventure.append(contador_Adventure) 
    Racing.append(contador_Racing )
    EarlyAccess.append(contador_EarlyAccess) 
    MassivelyMultiplayer.append(contador_MassivelyMultiplayer)
    AnimationModeling.append(contador_AnimationModeling)
    WebPublishing.append(contador_WebPublishing) 
    Education.append(contador_Education) 
    SoftwareTraining.append(contador_SoftwareTraining )
    Utilities.append(contador_Utilities )
    DesignIllustration.append(contador_DesignIllustration )
    AudioProduction.append(contador_AudioProduction)
    VideoProduction.append(contador_VideoProduction) 
    PhotoEditing.append(contador_PhotoEditing )
    

categorias_juegos = {
    'juego': juego,
    'Action': Action,
    'Casual': Casual,
    'Indie': Indie,
    'Simulation': Simulation,
    'Strategy':Strategy,
    'FreetoPlay':FreetoPlay ,
    'RPG': RPG,
    'Sports': Sports,
    'Adventure':Adventure ,
    'Racing':Racing ,
    'EarlyAccess':EarlyAccess ,
    'MassivelyMultiplayer':MassivelyMultiplayer ,
    'AnimationModeling': AnimationModeling,
    'WebPublishing': WebPublishing,
    'Education':Education ,
    'SoftwareTraining':SoftwareTraining ,
    'Utilities':Utilities ,
    'DesignIllustration':DesignIllustration ,
    'AudioProduction': AudioProduction,
    'VideoProduction':VideoProduction ,
    'PhotoEditing' : PhotoEditing
}

df = pd.DataFrame(categorias_juegos)
df.to_csv("matriz_datos_juegos.csv",index= False)