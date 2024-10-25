# Encuesta Flask

Este es un proyecto básico de una aplicación web de encuesta construida con Flask y Flask-WTF. La aplicación permite a los usuarios completar una encuesta, y sus respuestas se almacenan en una base de datos **DuckDB**.

## Pasos

1. **Crear la tabla en DuckDB:**
   Ejecuta el archivo `create_table.py` para crear la tabla necesaria en la base de datos DuckDB.

2. **Iniciar la aplicación Flask:**
   Ejecuta app.py para iniciar la aplicación Flask.

3. **(Opcional) Realizar una consulta SQL a la base de datos:**
   Abre y ejecuta el archivo query.ipynb en Jupyter Notebook para realizar consultas SQL a la base de datos y analizar las respuestas de la encuesta.

## Requisitos
- Python 3.7+
- DuckDB para manejar la base de datos
- Flask y Flask-WTF para la aplicación y el manejo de formularios 
