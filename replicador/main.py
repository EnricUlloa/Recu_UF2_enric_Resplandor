from fastapi import FastAPI, Form
from services.user import create_table, fill_user, obtain_user, update_user, delete_user

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

@app.get("/formulario/registro/{id]", response_model=dict)
async def obtener(id: int):
    result = await obtain_user(id)
    return result

@app.put("/formulario/registro/{id}", response_model=dict)
async def modificar(id: int, apellido: str, direccion: str):
    result = await update_user(id, apellido, direccion)
    return result

@app.delete("/formulario/registro/{id}", response_model=dict)
async def eliminar(id: int):
    result = await delete_user(id)
    return result