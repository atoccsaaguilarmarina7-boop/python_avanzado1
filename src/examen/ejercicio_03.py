##3. Type-hints (Anotaciones de tipo) 
# Diseña una función llamada obtener_promedio que reciba una lista de números enteros (list[int]) y retorne
# un número flotante (float) que represente el promedio de los valores. Incluye las anotaciones de tipo
#  estrictas vistas en el apunte. 

def obtener_promedio(numeros: list[int]) -> float:
    promedio: float = sum(numeros) / len(numeros)
    return promedio
numeros: list[int] = [15, 18, 16, 20, 14]
resultado: float = obtener_promedio(numeros)
print("El promedio es:", resultado)