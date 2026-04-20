from fastapi import FastAPI, Form
from services.user import create_table, fill_user

app = FastAPI()

create_table()

@app.post("/formulario/registro", response_model=dict)
async def insertar(
        nombre: str = Form(...),
        apellido: str = Form(...),
        email: str = Form(...),
        descripcion: str = Form(None),
        curso: str = Form(...),
        anio: int = Form(...),
        direccion: str = Form(...),
        cp: int = Form(None),
        password: str = Form(...)
    ):
    result = await fill_user(nombre, apellido, email, descripcion, curso, anio, direccion, cp, password)
    return result