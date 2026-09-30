# analisis_funciones.py
# Reescribiendo el analisis del Modulo 1 usando funciones
 
import pandas as pd
 
 
def cargar_datos(ruta_csv):
    """Carga el CSV y devuelve un DataFrame."""
    df = pd.read_csv(ruta_csv)
    print(f"Cargadas {len(df)} filas desde {ruta_csv}")
    return df
 
 
def promedio_por_grupo(df, variable, grupo):
    """Calcula el promedio de una variable agrupada por una o varias columnas.
 
    Parametros:
        df: el DataFrame
        variable: nombre de la columna numerica (ej: "ingreso")
        grupo: nombre de columna o lista (ej: "sexo" o ["sexo", "area"])
    """
    return df.groupby(grupo)[variable].mean().round(0)
 
def mediana_por_grupo(df, variable, grupo):
    """Calcula la mediana de una variable, agrupada por una o varias columnas.

    Parametros
    ----------
    df : pandas.DataFrame
        El DataFrame con los datos.
    variable : str
        Nombre de la columna numerica sobre la que calcular el promedio.
    grupo : str o list
        Columna o lista de columnas por las que agrupar.

    Devuelve
    --------
    pandas.Series
        Mediana redondeada al entero mas cercano.

    Ejemplo
    -------
    >>> mediana_por_grupo(df, "ingreso", "sexo")
    >>> mediana_por_grupo(df, "ingreso", ["sexo", "area"])
    """
    return df.groupby(grupo)[variable].median().round(0)

# Cargar una vez, usar la funcion muchas veces
df = cargar_datos("datos_ejemplo.csv")
 
print("\nIngreso promedio por sexo:")
print(promedio_por_grupo(df, "ingreso", "sexo"))
 
print("\nIngreso promedio por area:")
print(promedio_por_grupo(df, "ingreso", "area"))
 
print("\nIngreso promedio por sexo y area:")
print(promedio_por_grupo(df, "ingreso", ["sexo", "area"]))
 
print("\nEdad promedio por sexo:")
print(promedio_por_grupo(df, "edad", "sexo"))

print("\nEdad mediana por sexo y area:")
print(mediana_por_grupo(df, "edad", ["sexo", "area"]))
