##5. Empaquetado Nominal (**kwargs)
#  Diseña una función llamada generar_perfil_usuario(**kwargs) que reciba datos arbitrarios en formato 
# clave-valor (como nombre, edad, país, profesión) y devuelva una cadena de texto descriptiva que recorra el 

def generar_perfil_usuario(**kwargs) -> str:
    perfil = ""

    for clave, valor in kwargs.items():
        perfil += f"{clave}: {valor}\n"

    return perfil
resultado = generar_perfil_usuario(
    nombre="carla",
    edad=20,
    pais="Peru",
    profesion="Estudiante"
)
print("PERFIL DEL USUARIO")
print(resultado)