from pydantic import BaseModel


class CourseBase(BaseModel):
    title: str
    description: str
    duration_weeks: int
    department_id: int
    teacher_id: int


class CourseCreate(CourseBase):
    pass


class Course(CourseBase):
    id: int

    class Config:
        orm_mode = True
