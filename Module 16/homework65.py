from fastapi import FastAPI, status, Body, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi import Path
from typing import Annotated
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')
users = []

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get('/')
async def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'list_of_users': users})

@app.get('/users/{user_id}')
async def get_users(request: Request, user_id: id(users)) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'user': user_id})

@app.post('/user/{username}/{age}')
async def create_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')], age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=24)]) -> str:
    new_id = 1 if not users else users[-1].id + 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user

create_user('UrbanUser', 24)
create_user('UrbanTest', 22)
create_user('Capybara', 60)

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example=1)], username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')], age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=24)]) -> int:
    try:
        for user in users:
            if user.id == user_id:
                user.username = username
                user.age = age
                return user
    except IndexError:
        raise HTTPException(status_code=404, detail="User  was not found")


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example=1)]) -> str:
    try:
        for index, user in enumerate(users):
            if user.id == user_id:
                deleted_user = users.pop(user_id)
                return deleted_user
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')