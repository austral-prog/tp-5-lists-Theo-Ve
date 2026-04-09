# Ejercicio 12: Manipular lista de listas

def list_of_lists(lista_de_listas):
    # Modifica una lista de 3 listas: toma los primeros 2 elementos de la primera,
    # los elementos del índice 1 al 3 de la segunda y los últimos 2 de la tercera
    primera = lista_de_listas[0][0:2]
    segunda = lista_de_listas[1][1:4]
    tercero = lista_de_listas[2][-2:]
    return [primera, segunda, tercero]