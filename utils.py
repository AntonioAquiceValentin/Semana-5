# --------MÓDULO UTILS------------

#Crea un módulo utils.py con funciones que usen *args y **kwargs para manejar cantidad variable de parámetros.

def sumar_todos(*args):
    """Suma cualquier cantidad de números que le pases."""
    return sum(args)

def imprimir_info(**kwargs):
    """Imprime cualquier dato que le pases con nombre."""
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")