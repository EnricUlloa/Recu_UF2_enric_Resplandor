def user_schema(result) -> dict:
    return {
        "id": result[0],
        "nombre": result[1],
        "apellido": result[2],
        "email": result[3],
        "curso": result[4],
        "anio": result[5],
        "direccion": result[6],
    }