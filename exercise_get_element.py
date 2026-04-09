# Ejercicio 2: Obtener elemento en posición específica

def get_element(lista, indice):
    if indice > len(lista):     # Verifica si el índice es mayor al tamaño de la lista (fuera de rango positivo)
        return None
    elif indice < len(lista)*-1:     # Verifica si el índice es menor que el rango negativo permitido
        return None
    elif lista == []:   # Verifica si la lista no tiene ningun elemento
        return None
    else:         # Retorna el elemento en la posición indicada
        return lista[indice]