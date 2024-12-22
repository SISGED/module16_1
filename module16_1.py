from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def main_page():
    return "Главная страница"

@app.get("/user")
async def user(username: str, age: int) -> dict:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

@app.get("/user/{user_id}")
async def id(user_id: int):
    return f"Вы вошли как пользователь №{user_id}!"

@app.get("/user/admin")
async def admin():
    return"Вы вошли как администратор!"

