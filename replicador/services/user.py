from config import database

def create_table():
    conn = database.connection_db()
    cursor = conn.cursor()
    sql_table = '''
        CREATE TABLE IF NOT EXISTS users(
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            apellido VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            descripcion TEXT,
            curso VARCHAR(100) NOT NULL,
            anio INTEGER NOT NULL,
            direccion VARCHAR(100) NOT NULL,
            cp INTEGER,
            password VARCHAR(100) NOT NUll
        )
    '''
    cursor.execute(sql_table)
    conn.commit()
    cursor.close()
    conn.close()
    print("Tabla creada correctamente")

async def fill_user(nombre, apellido, email, descripcion, curso, anio, direccion, cp, password):
    conn = database.connection_db()
    cursor = conn.cursor()
    sql_post = "INSERT INTO users (nombre, apellido, email, descripcion, curso, anio, direccion, cp, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (nombre, apellido, email, descripcion, curso, anio, direccion, cp, password)
    cursor.execute(sql_post, values)
    conn.commit()
    cursor.close()
    conn.close()
    return{"mensaje": "Usuario creado correctamente"}