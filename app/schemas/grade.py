from datetime import date

from pydantic import BaseModel


class GradeBase(BaseModel):
    student_id: int
    course_id: int
    exam_id: int
    grade_value: int
    date: date


class GradeCreate(GradeBase):
    pass


class GradeUpdate(GradeBase):
    pass


class Grade(GradeBase):
    id: int

    class Config:
        orm_mode = True
