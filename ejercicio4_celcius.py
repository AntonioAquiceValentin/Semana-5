# Importa el módulo conversor
import ejercicio4_conversor

# Solicita los grados Celsius
c = float(input("Ingrese los grados Celsius: "))
print("Fahrenheit:", ejercicio4_conversor.celsius_a_fahrenheit(c))

# Solicita los grados Fahrenheit
f = float(input("Ingrese los grados Fahrenheit: "))
print("Celsius:", ejercicio4_conversor.fahrenheit_a_celsius(f))