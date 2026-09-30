# primeras_funciones.py
# Aprendiendo a escribir funciones en Python
 
def cuadrado(x):
    """Devuelve el cuadrado de un numero."""
    return x * x
 
 
def es_mayor_de_edad(edad):
    """Devuelve True si la edad es 18 o mas, False de lo contrario."""
    return edad >= 18
 
 
def saludo(nombre, formal=False):
    """Construye un saludo personalizado.
 
    Si formal=True usa un saludo formal, de lo contrario uno casual.
    """
    if formal:
        return f"Buenos dias, Sr./Sra. {nombre}"
    else:
        return f"Hola, {nombre}!"
 
 
# Ejecutar las funciones para ver que devuelven
print(cuadrado(5))
print(cuadrado(12))
print(es_mayor_de_edad(20))
print(es_mayor_de_edad(15))
print(saludo("Ana"))
print(saludo("Ana", formal=True))
