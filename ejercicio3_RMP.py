#Crea una función agregar(lista, elemento) que añada el 
# elemento al final de la lista. ¿Cambia fuera?

def agregar(lista, elemento):
     lista.append(elemento)
     print(f"dentro: {lista} ")


Mi_lista = [1,2,3,4,5]
agregar (Mi_lista, 195)
print(f" fuera {Mi_lista}")
