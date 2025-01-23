"""
CreateUser с атрибутами: username(str), firstname(str), lastname(str) и age(int)
UpdateUser с атрибутами: firstname(str), lastname(str) и age(int)
CreateTask с атрибутами: title(str), content(str), priority(int)
UpdateTask с теми же атрибутами, что и CreateTask.
"""
from pydantic import BaseModel


class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int


class UpdateUser(CreateUser):
    pass


class CreateTask(BaseModel):
    title: str
    content: str
    priority: int


class UpdateTask(CreateTask):
    pass
