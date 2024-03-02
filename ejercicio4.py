import math
from decimal import Decimal

# ejercicio 1

n_entero = 1
n_flotante = 0.5
n_decimal = Decimal('3.14') # especificamente decimal 


my_lista = [n_entero, n_decimal, n_flotante]
my_tupla = (n_entero, n_decimal, n_flotante)
my_diccionario = { 
      "n_e" : n_entero,
      "n_f" : n_flotante,
      "n_d" : n_decimal         
}

print("my lista es: ", my_lista)
print("my tupla es: ", my_tupla)
print("my diccionario es: ", my_diccionario)

print(type(n_entero))
print(type(n_flotante))
print(type(n_decimal))

# ejercicio 2

print(math.ceil(n_flotante))

# ejercicio 3

print(math.sqrt(n_flotante))

# ejercicio 4

print (my_diccionario.items())
my_diccionario_elementos = list(my_diccionario.copy().items())
print(my_diccionario_elementos[0])

# ejercicio 5

print(my_tupla[1])

# ejercicio 6

my_lista.append(-5)
print(my_lista)

# ejercicio 7

my_lista[0]= 7
print(my_lista)

# ejercicio 8

my_lista.sort() 
print(my_lista)

# ejercicio 9

n_primo = 11
# my_tupla += (n_primo,) 
my_tupla = my_tupla + (n_primo,) 
print(my_tupla)