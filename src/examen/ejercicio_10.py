##10. Programación Funcional (filter()) 
# Dada una lista de palabras: palabras: list[str] = ["sol", "computadora", "luz", "programacion", "ia", "python"],
#  utiliza la función integrada filter() y una función lambda para filtrar y quedarte únicamente con aquellas 
# palabras que tengan más de 4 caracteres. Muestra el resultado convertido en lista. 

palabras: list[str] = ["sol", "computadora", "luz", "programacion", "ia", "python"]
palabras_filtradas = list(filter(lambda x: len(x) > 4, palabras))
print("Lista original:", palabras)
print("Palabras con más de 4 caracteres:", palabras_filtradas)