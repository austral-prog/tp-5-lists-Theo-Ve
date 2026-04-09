# Ejercicio 6: Encontrar el mínimo en una lista

def find_min(lista):
    if len(lista) == 0: # Devuelve el valor mínimo de la lista; si está vacía, retorna "None"
        return None
    else:
        return min(lista)