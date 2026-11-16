##7. Documentación (docstring) 
# Crea una función llamada calcular_potencia(base: float, exponente: float) -> float que eleve un número a su
#  potencia. Añade un docstring completo que cumpla estrictamente con la advertencia del apunte: 
#1. Breve explicación.
#  2. Especificación y tipos de los parámetros.
#  3. Restricciones (ej. el exponente no debe ser negativo). 
# 4. Características del valor que retorna. 

def calcular_potencia(base: float, exponente: float) -> float:
    """
    Calcula la potencia de un número elevado a un exponente.

    Parámetros:
        base (float): Número que se desea elevar.
        exponente (float): Potencia a la que se elevará la base.

    Restricciones:
        El exponente no debe ser negativo.
        La base y el exponente deben ser números reales.

    Retorna:
        float: El resultado de elevar la base al exponente.
    """

    if exponente < 0:
        raise ValueError("El exponente no debe ser negativo")

    resultado = base ** exponente
    return float(resultado)

resultado = calcular_potencia(2.0, 3.0)

print("El resultado de la potencia es:", resultado)