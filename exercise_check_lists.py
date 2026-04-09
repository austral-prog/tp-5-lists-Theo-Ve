# Ejercicio 11: Comparar tercer elemento de dos listas

def check_lists(lista1, lista2): # Verifica si ambas listas tienen al menos 3 elementos y si sus terceros elementos son iguales
    if len(lista1) > 2 and len(lista2) > 2:
        if lista1[2] == lista2[2]:
            return True
        else:
            return False
    return False