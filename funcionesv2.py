print("Funciones version 2")
print("Paola Ramirez")
# zona de listas, tuplas, conjuntos y diccionario
celulares = ["Samsung a52" ,"Iphone 11" ,"Chafa"]
animales = ("Perro" ,"Gato" ,"Conejo")
artistas = {"Selena Quintanilla" ,"Juan Gabriel" ,"Jose Jose"}
canciones = {
    "Rock" : "Astaroth",
    "Pop"  : "Smooth Criminal",
    "Khh"  : "Mommae"
}
# zona de funciones
def verlista(telefonos):
    for uncelular in telefonos:
        print(uncelular)
def vertupla(animal):
    for unanimal in animal:
        print(unanimal)
def verconjunto(artista):
    for unartista in artista:
        print(unartista)
def verdiccionario(cancion):
    for unacancion, musica in cancion.items():
        print(unacancion, musica)
# llama a funciones
print("Imprime celulares de una lista")
verlista(celulares)
print("Imprime animales de una tupla")
vertupla(animales)
print("Imprime artistas de un conjunto")
verconjunto(artistas)
print("Imprime canciones de un diccionario")
verdiccionario(canciones)