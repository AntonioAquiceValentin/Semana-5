#-----------MÓDULO PROPIO-------------------
#Conversor de celsius y fahrenheit

#Crea un módulo conversor.py con funciones celsius_a_fahrenheit y fahrenheit_a_celsius y úsalas.

def celsius(fah):
    c = (fah-32) / 1.8
    c = round(c, 2)
    return (f"{fah}°F es {c}° C")

# y = float(input("Ingresa los grados Fahrenheit: "))
# x = celsius(y)

def fahrenheit(cel):
    f = (cel * 1.82) + 32
    f = round(f, 2)
    return (f"{cel}°C es {f}° F")

# k = float(input("Ingresa los grados Celsius: "))
# o = celsius(k)