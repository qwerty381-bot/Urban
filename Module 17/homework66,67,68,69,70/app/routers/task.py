from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from typing import Annotated
from models import Task
from schemas import CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete
from slugify import slugify

router = APIRouter(prefix='/task', tags=['task'])

@router.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task).where(Task.is_active == True)).all()
    return tasks

@router.get('/task_id')
async def task_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    task = db.scalar(select(Task).where(Task.is_active == True))
    if task is None:
        raise HTTPException(status_code=404, detail='User was not found')
    return task

@router.post('/create')
async def create_task(db: Annotated[Session, Depends(get_db)], create_task: CreateTask):
    db.execute(insert(Task).values(
        username=create_task.name,
        firstname=create_task.firstname,
        lastname=create_task.lastname,
        age=create_task.age,
        slug=slugify(create_task.firstname)))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }

@router.put('/update')
async def update_task(db: Annotated[Session, Depends(get_db)], user_id: int, update_task: UpdateTask):
    user = db.scalar(select(Task).where(Task.id == user_id))
    if user is None:
        raise HTTPException(status_code=404, detail='User was not found')
    db.execute(update(Task).where(Task.id == user_id).values(
            firstname=update_task.firstname,
            lastname=update_task.lastname,
            age=update_task.age,
            slug=slugify(update_task.firstname)))
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'User Update is successful!'
    }

@router.delete('/delete')
async def delete_task(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(Task).where(Task.id == user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='There is no user found')
    db.execute(delete(Task).where(Task.id == user_id))
    db.commit()
    return {
        'status_code': status.HTTP_404_NOT_FOUND,
        'transaction': 'User delete is successful!'
    }