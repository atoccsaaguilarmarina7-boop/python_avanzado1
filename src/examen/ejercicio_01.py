##1. Funciones Básicas 
# Crea una función llamada calcular_area_rectangulo que reciba la base y la altura de un rectángulo (números enteros o flotantes) 
# y retorne su área calculada. Pruébala llamándola con dos valores distintos e imprime el resultado. 
# Crear una función anónima con lambda


calcular_area_rectangulo = lambda base, altura: base * altura
print("Area del primer rectangulo:",
      calcular_area_rectangulo(5, 10))
print("Area del segundo rectangulo:",
      calcular_area_rectangulo(4.5, 3.2))