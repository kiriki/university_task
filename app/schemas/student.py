from datetime import date

from fastapi import FastAPI
from pydantic import BaseModel

from . import GenderEnum

app = FastAPI()


class StudentBase(BaseModel):
    first_name: str
    last_name: str
    birth_date: date
    gender: GenderEnum
    phone: str
    admission_date: date
    group_id: int


class StudentCreate(StudentBase):
    pass


class StudentUpdate(StudentBase):
    pass


class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True
        use_enum_values = True
