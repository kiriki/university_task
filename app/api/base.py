from fastapi import APIRouter

from .route import courses, grades, students, teachers

api_router = APIRouter()

api_router.include_router(students.router, tags=['students'], prefix='/students')
api_router.include_router(teachers.router, tags=['teachers'], prefix='/teachers')
api_router.include_router(courses.router, tags=['courses'], prefix='/courses')
api_router.include_router(grades.router, tags=['grades'], prefix='/grades')
