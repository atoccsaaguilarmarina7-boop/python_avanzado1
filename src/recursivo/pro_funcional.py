# ejercicio 1: Tienes una lista de temperaturas (algunas bajo cero),
# filtra la lista para quedarte solo con las temperaturas positivas
# (mayores a 0).

temp_list = [-2, 10, 0, -25, -7, -12, 18, 23, 0]

nueva_tem = list(filter(lambda t: t > 0, temp_list))

print(f"Las temperaturas mayores a cero son: {nueva_tem}")
# ejercicio combinando map() y filter()

# Tienes una lista de numeros. Primero filtra para quedarte solo con
# los numeros pares. Luego usa map para multiplicarlos por 10 los
# numeros pares.

num: list[int] = [2, 3, 4, 6, 7, 9, 11, 12, 15, 17, 19]

numeros_pares: list[int] = list(filter(lambda n: n % 2 == 0, num))
por_diez: list[int] = list(map(lambda n: n * 10, numeros_pares))
# por_diez en una sola linea:
por_diez: list[int] = list(map(lambda n: n * 10, filter(lambda n: n % 2 == 0, num)))


