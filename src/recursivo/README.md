# Funciones en python
## Programación funcional

Python es un lenguaje de programación multiparadigma, y uno de sus paradigmas que mejor funciona es la funcional.

Python usa como `map()`, `filter()`, `reduce()`, entre otras, para procesar datos.

Estas funciones integradas de python sirven para procesar y transformar colecciones de datos (listas, diccionarios) de manera eficiente.

### 1. map()

Es una función de orden superior, recibe dos parámetros: primero la función a ejecutar y segundo el iterable en el que va a actuar.

map aplica una función específica a cada uno de los elementos de una colección (iterable) y devuelve un nuevo iterable con los resultados.
# de un lista desemos calcualr la potenca de cada numero

numeros = [1, 2, 3, 4, 5, 6, 7]

# Cuando declaramos una función anónima tenemos que
# declarar primero la función antes de pasarla por parámetro

def cuadrado(x):
    return x ** 2

# Una vez creada pasamos la función como parámetro
cuadrados = list(map(cuadrado, numeros))
print(cuadrados)

# Cuando deseamos trabajar con funciones anónimas usamos lambda dentro del parámetro
cuadrados_lambda = list(map(lambda x: x ** 2, numeros))
print(cuadrados_lambda)
### 2.fiter()
filter pasa a cad elemento



# filter también es función de orden superior,
# recibe una función que devuelve True o False
# y solo se queda con los que dan True

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Con función normal
def es_par(x):
    return x % 2 == 0

pares = list(filter(es_par, numeros))
print(pares)

# Con lambda, que es lo mismo pero más corto
pares_lambda = list(filter(lambda x: x % 2 == 0, numeros))
print(pares_lambda)
### 2. filter()

filter aplica una función que devuelve True o False a cada uno de los elementos de una colección (iterable) y devuelve un nuevo iterable solo con los elementos que cumplen la condición.

Es decir, filter sirve para filtrar, para quedarse solo con los datos que nos interesan.

Ejemplo:
```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares) # [2, 4, 6, 8, 10]

