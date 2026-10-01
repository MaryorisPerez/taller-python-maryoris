# ejercicio_ia.py
# Ejercicio del Modulo 4: usar IA para extender analisis_v2.py.
#
# Este archivo es el PUNTO DE PARTIDA. Tu mision es extenderlo con ayuda
# de tu asistente de IA preferido (Copilot, Cursor, Continue, Cline, etc.)
# para agregar las funcionalidades descritas mas abajo.
#
# Recomendacion: trabajalo en TU REPO de GitHub para que quede commit
# de cada mejora. Asi puedes ver tu progreso y cuanto del codigo final
# fue generado por IA vs escrito por ti.

import argparse
import os
from datetime import datetime
from functools import wraps

import pandas as pd
from analisis_v2 import cargar_datos, promedio_por_grupo, exportar_a_excel


# ============================================================================
# TAREAS PARA HACER CON AYUDA DE IA
# ============================================================================
#
# Tarea 1 (FACIL):
#   Agrega una funcion percentil_por_grupo(df, variable, grupo, p) que
#   devuelva el percentil p (entre 0 y 100) de la variable, agrupado por
#   las columnas especificadas. Documentala con docstring.
#
# Tarea 2 (MEDIA):
#   Agrega validacion al inicio de main(): si datos_ejemplo.csv no existe,
#   imprime un mensaje claro indicando que el usuario debe correr primero
#   generar_datos.py. Termina la ejecucion limpiamente sin un traceback.
#
# Tarea 3 (MEDIA):
#   Agrega logging basico a las funciones existentes. Que cada funcion
#   imprima un mensaje cuando empieza y cuando termina, con un timestamp.
#   Pista: from datetime import datetime
#
# Tarea 4 (DIFICIL):
#   Refactoriza main() para que reciba como argumento la ruta del CSV
#   de entrada. Si se llama sin argumentos, usa "datos_ejemplo.csv" por
#   defecto. Pista: investiga el modulo sys.argv o argparse.
#
# ============================================================================


# NOTA: main() y el bloque if __name__ == "__main__" se movieron al final
# del archivo, despues de las funciones de cada tarea.


# ============================================================================
# REFLEXION AL FINAL
# ============================================================================
#
# Al terminar las 4 tareas, dedica 10 minutos a estas preguntas (escribe
# tus respuestas como comentarios en este mismo archivo o como un Issue
# en tu repo):
#
# 1. Cual tarea te resulto mas dificil de pedirle a la IA?
#    Que termino haciendo IA y que terminaste haciendo tu?
#
# 2. Cuantas veces la IA propuso algo INCORRECTO o subóptimo y tuviste
#    que pedirle que lo ajustara?
#
# 3. En que parte sentiste que la IA te ahorro mas tiempo? En que parte
#    sentiste que te lo hizo perder?
#
# 4. Si vuelves a hacer este mismo ejercicio mañana, que harias diferente
#    en como pides ayuda?
#
# ============================================================================


# FACIL
def percentil_por_grupo(df, variable, grupo, p):
    """Calcula el percentil p de una variable, agrupada por una o varias columnas.

    Parametros
    ----------
    df : pandas.DataFrame
        El DataFrame con los datos.
    variable : str
        Nombre de la columna numerica sobre la que calcular el percentil.
    grupo : str o list
        Columna o lista de columnas por las que agrupar.
    p : int o float
        Percentil a calcular, entre 0 y 100 (por ejemplo, 50 es la mediana).

    Devuelve
    --------
    pandas.Series
        Percentiles redondeados al entero mas cercano.

    Ejemplo
    -------
    >>> percentil_por_grupo(df, "ingreso", "sexo", 50)
    >>> percentil_por_grupo(df, "ingreso", ["sexo", "area"], 90)
    """
    if not 0 <= p <= 100:
        raise ValueError(f"p debe estar entre 0 y 100, se recibio: {p}")
    return df.groupby(grupo)[variable].quantile(p / 100).round(0)


# MEDIA (Tarea 3)
def con_log(funcion):
    """Envuelve una funcion para que avise cuando empieza y cuando termina.

    Parametros
    ----------
    funcion : callable
        La funcion a la que se le quiere agregar logging.

    Devuelve
    --------
    callable
        La misma funcion, pero imprimiendo un mensaje con timestamp al
        empezar y al terminar.

    Ejemplo
    -------
    >>> cargar_datos = con_log(cargar_datos)
    >>> df = cargar_datos("datos_ejemplo.csv")
    """
    @wraps(funcion)
    def envoltura(*args, **kwargs):
        print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] Empieza {funcion.__name__}")
        try:
            return funcion(*args, **kwargs)
        finally:
            print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] Termina {funcion.__name__}")
    return envoltura


# Se aplica el logging a las funciones existentes sin modificar analisis_v2.py
cargar_datos = con_log(cargar_datos)
promedio_por_grupo = con_log(promedio_por_grupo)
exportar_a_excel = con_log(exportar_a_excel)
percentil_por_grupo = con_log(percentil_por_grupo)


# MEDIA (Tarea 2) y DIFICIL (Tarea 4)
@con_log
def main():
    """Corre el analisis sobre el CSV indicado por linea de comandos.

    Si se llama sin argumentos usa "datos_ejemplo.csv". Si el archivo no
    existe, imprime un mensaje claro y termina sin traceback.

    Ejemplo
    -------
    python ejercicio_ia.py
    python ejercicio_ia.py otros_datos.csv
    """
    # Tarea 4: ruta del CSV como argumento opcional
    parser = argparse.ArgumentParser(description="Analisis de ingresos por grupo.")
    parser.add_argument(
        "ruta_csv",
        nargs="?",
        default="datos_ejemplo.csv",
        help="Ruta del CSV de entrada (por defecto: datos_ejemplo.csv)",
    )
    ruta_csv = parser.parse_args().ruta_csv

    # Tarea 2: validar que el archivo exista antes de cargarlo
    if not os.path.exists(ruta_csv):
        print(f"ERROR: no se encontro el archivo '{ruta_csv}'.")
        print("Corre primero generar_datos.py para crearlo:")
        print("    python generar_datos.py")
        return

    df = cargar_datos(ruta_csv)

    print("\nIngreso promedio por sexo y area:")
    print(promedio_por_grupo(df, "ingreso", ["sexo", "area"]))

    # Tarea 1: ejemplos de uso de percentil_por_grupo
    print("\nMediana (percentil 50) del ingreso por sexo:")
    print(percentil_por_grupo(df, "ingreso", "sexo", 50))

    print("\nPercentil 90 del ingreso por sexo y area:")
    print(percentil_por_grupo(df, "ingreso", ["sexo", "area"], 90))


if __name__ == "__main__":
    main()
