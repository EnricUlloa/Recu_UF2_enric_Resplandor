import psycopg2

def connection_db():
    conn = psycopg2.connect(
        database="postgres",
        password="pass_postgres",
        user="user_postgres",
        host="localhost",
        port="5432"
    )
    print("Conexion establecida")
    return conn

#connection_db()