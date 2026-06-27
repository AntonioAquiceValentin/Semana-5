# Diccionario que almacena el inventario
inventario = {}

# Agregar un producto
def agregar(inventario, producto, cantidad):
    inventario[producto] = cantidad

# Actualizar la cantidad de un producto
def actualizar(inventario, producto, cantidad):
    inventario.update({producto: cantidad})

# Listar todos los productos
def listar(inventario):
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("Inventario:")
        for producto, cantidad in inventario.items():
            print(f"- {producto}: {cantidad}")

# Ejemplo de uso
agregar(inventario, "Manzanas", 50)
agregar(inventario, "Peras", 30)
actualizar(inventario, "Manzanas", 60)

listar(inventario)