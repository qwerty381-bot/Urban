from fastapi import FastAPI

app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def get1() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def post1(username: str, age: int) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is registered'

@app.put('/user/{user_id}/{username}/{age}')
async def put1(user_id: str, username: str, age: int) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is updated'

@app.delete('/user/{user_id}')
async def delete1(user_id: str) -> str:
    users.pop(user_id)
    return f'The user {user_id} has been deleted'