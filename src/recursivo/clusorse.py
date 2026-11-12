# de crear una funcion tipo closure que me permita
# ingresar nombre, apellidos y me retorne un mensaje con
# ambos datos.

def creador(nombre: str):
    def apellido(ap: str) -> str:
        return f"tu nombre es {nombre} y tu apellido es {ap}"
    return apellido

alumno1 = creador("david") #def apellidov(ap):return
print(alumno1("goliat"))

## usando clusorse crea una funcion multiplicador que reciva comparmetros 
# el factor que devuelva una funcion que permi9ta doplificar culaquer numero por el factor 
def multiplicador(factor: int):
    def por_numero(ap: int) -> int:
        return factor * ap
    return por_numero

doble = multiplicador(2)
print(doble(5)) #10