# prueba_import.py
# Demostracion: importar funciones del analisis_v2.py
 
from analisis_v2 import cargar_datos, promedio_por_grupo
 
df = cargar_datos("datos_ejemplo.csv")
print("\nEdad promedio por sexo (calculado importando funciones):")
print(promedio_por_grupo(df, "edad", "sexo"))

