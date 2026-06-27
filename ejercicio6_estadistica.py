# Calcula el promedio de una lista
def promedio(lista):
    return sum(lista) / len(lista)

# Devuelve el número mayor
def maximo(lista):
    mayor = lista[0]

    for numero in lista:
        if numero > mayor:
            mayor = numero

    return mayor

# Devuelve el número menor
def minimo(lista):
    menor = lista[0]

    for numero in lista:
        if numero < menor:
            menor = numero

    return menor