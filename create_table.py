import duckdb

# Connect to DuckDB
con = duckdb.connect('C:\\Users\\usuario\\Desktop\\Proyectos\\GUILLE\\PGB\\Formulario Flask\\coffeecms.duckdb')

# Drop the table if it already exists
con.execute("DROP TABLE IF EXISTS users")

# Create the table with the appropriate columns
con.execute("""
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    fantasia VARCHAR(255) NOT NULL,
    cuit INTEGER NOT NULL
)
""")

# Close the connection
con.close()
