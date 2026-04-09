# Ejercicio 5: Encontrar el máximo en una lista

def find_max(lista):
    if len(lista) == 0: # Devuelve el valor máximo de la lista; si está vacía, retorna "None"
        return "None"
    else:
        return max(lista)
