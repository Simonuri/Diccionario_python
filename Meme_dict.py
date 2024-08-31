meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    'PARCERO':"Amigo"
    }


for i in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Esa palabra no esta en el diccionario")
        # ¿Qué hacer si no se encuentra la palabra?
