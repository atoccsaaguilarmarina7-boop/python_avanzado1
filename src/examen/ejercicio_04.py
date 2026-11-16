##4. Empaquetado Posicional (*args)
#  Crea una función llamada unir_frases(*args) que reciba una cantidad variable de cadenas de texto (str) y las 
# una en una sola oración separadas por un espacio, retornando el resultado final.

def unir_frases(*args: str) -> str:
    resultado = " ".join(args)
    return resultado
frase = unir_frases(
    "Hola",
    "mi nombre es Marina",
    "y estoy aprendiendo Python"
)
print("La frase completa es:", frase) 