from datetime import date

from pydantic import BaseModel

from . import GenderEnum


class TeacherBase(BaseModel):
    first_name: str
    last_name: str
    birth_date: date
    gender: GenderEnum
    phone: str
    hire_date: date


class Teacher(TeacherBase):
    id: int

    class Config:
        orm_mode = True
        use_enum_values = True
