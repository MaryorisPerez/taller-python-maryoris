# Taller de Python — Maryoris Pérez Sánchez

Repositorio personal del taller "Python para Analistas Estadísticos" (DANE).

## Sobre este repositorio

Este repo contiene mis avances de los módulos del taller: mis primeros scripts, el análisis de un dataset sintético de 100 personas (edad, sexo, ingreso y área), su migración de un notebook Jupyter a un script modular con funciones, y el material de referencia de cada módulo. El objetivo es construir una base sólida de Python, control de versiones con Git/GitHub y uso de IA para desarrollo.

## Estructura

```
.
├── hola.py                  # Mi primer script (Módulo 1)
├── generar_datos.py         # Genera el dataset sintético datos_ejemplo.csv (Módulo 1)
├── datos_ejemplo.csv        # Dataset sintético: id, edad, sexo, ingreso, area
├── analisis.ipynb           # Notebook Jupyter del análisis exploratorio (Módulo 2)
├── analisis_v2.py           # Análisis modularizado en funciones (Módulo 2)
├── prueba_import.py         # Prueba de importar funciones desde analisis_v2.py (Módulo 2)
├── resumen.xlsx             # Resumen exportado a Excel por analisis_v2.py
├── modulo_1/                # Material de referencia y soluciones de retos del Módulo 1
├── modulo_2/                # Material de referencia del Módulo 2
├── modulo_3/                # Plantillas para el repo en GitHub (Módulo 3)
├── modulo_4/                # Material de IA en el IDE (Módulo 4)
└── README.md                # Este archivo
```

## Qué hace el análisis

`analisis_v2.py` organiza el análisis en funciones reutilizables, cada una con su docstring:

- `cargar_datos()` — carga el CSV en un DataFrame.
- `promedio_por_grupo()` / `mediana_por_grupo()` — promedio o mediana de una variable agrupada por una o varias columnas.
- `conteo_por_categoria()` — frecuencias de una variable categórica.
- `exportar_a_excel()` — guarda un resultado en un archivo `.xlsx`.
- `main()` — orquesta todo: conteo por sexo, ingreso promedio por sexo y por área, cruce sexo × área y edad promedio por área.

Gracias al bloque `if __name__ == "__main__":`, el archivo se puede ejecutar como script o importar como módulo (ver `prueba_import.py`).

## Cómo correr el código

Asumiendo que ya está clonado el repo:

```powershell
# 1. Crear y activar el entorno virtual
python -m venv .venv
.venv\Scripts\activate

# 2. Instalar dependencias
pip install pandas numpy openpyxl

# 3. Generar los datos (la primera vez)
python generar_datos.py

# 4. Correr el análisis
python analisis_v2.py

# 5. (Opcional) Probar la importación de funciones
python prueba_import.py
```

## Sobre el taller

El taller cubre cinco módulos secuenciales:

| Módulo | Tema |
|---|---|
| 0 | Antes de empezar — instalación |
| 1 | Tu primer proyecto en Python |
| 2 | De Jupyter a `.py` — funciones |
| 3 | Git y GitHub — desarrollo colaborativo |
| 4 | IA en el IDE |

## Autoría

**Maryoris Mairen Pérez Sánchez** — DANE, 2026.
