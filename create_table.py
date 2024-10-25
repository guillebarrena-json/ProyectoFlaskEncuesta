import duckdb

# Conéctate a DuckDB
con = duckdb.connect('C:\\Users\\usuario\\Desktop\\Proyectos\\GUILLE\\PGB\\Formulario Flask\\coffeecms.duckdb')

# Eliminar la tabla si ya existe
con.execute("DROP TABLE IF EXISTS users")

# Crear la tabla sin restricciones de identidad
con.execute("""
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    fullname VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
)
""")

# Cerrar la conexión
con.close()
