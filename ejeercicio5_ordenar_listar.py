# Ordena la lista original
def ordenar_original(lista):
    lista.sort()

# Devuelve una copia ordenada de la lista
def copia_ordenada(lista):
    copia = lista.copy()
    copia.sort()
    return copia

# Lista de prueba
numeros = [8, 3, 6, 1, 5]

print("Lista original:", numeros)

ordenar_original(numeros)
print("Lista ordenada:", numeros)

numeros = [8, 3, 6, 1, 5]

nueva = copia_ordenada(numeros)
print("Lista original:", numeros)
print("Copia ordenada:", nueva)