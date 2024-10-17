print(" ")
print("Andres Noe Gomez Garcia 3°w 1184: practica 4 2do parcial")
print(" ")

#Se crea un diccionario 
traductor={
    "amor": "Love",
    "amigo": "Friend",
    "feliz": "Happy",
    "familia":"Family",
    "agua":"Water",
    "escuela":"School",
    "comida":"Comida",
    "casa": "House",
    "musica": "Music"
}
#Se le pide la palabra al usuario
palabra=str(input("Ingrese la palabra que desea traducir: "))
if palabra in traductor:#Si la palabra se encuentra en el diccionario 
    print(palabra,"En ingles es:", traductor[palabra])#Imprimira
else:#Si no
    print("Esa palabra no esta en el diccionario")#Imprimira