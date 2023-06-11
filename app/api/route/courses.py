from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.repository.courses import create_course_repo, get_course_by_id, get_students_by_course_id
from db.session import get_db
from schemas.course import Course, CourseCreate
from schemas.student import Student

router = APIRouter(
    responses={404: {'description': 'Not found'}},
)


# POST /courses - создать новый курс.
# GET /courses/{course_id} - получить информацию о курсе по его id.
# GET /courses/{course_id}/students - получить список всех студентов на курсе.


@router.post('/', description='Create a new course', response_model=Course)
def create_course(course: CourseCreate, db: Session = Depends(get_db)) -> Course:
    created_course = create_course_repo(db, course)
    return created_course


@router.get('/{course_id}', description='Get information about a course by its ID', response_model=Course)
def get_course(course_id: int, db: Session = Depends(get_db)) -> Course:
    db_course = get_course_by_id(db, course_id=course_id)
    if not db_course:
        raise HTTPException(status_code=404, detail='Course not found')
    return db_course


@router.get(
    '/{course_id}/students', description='Get a list of all students in the course', response_model=list[Student]
)
def get_students(course_id: int, db: Session = Depends(get_db)) -> list[Student]:
    course = get_course_by_id(db, course_id=course_id)
    if not course:
        raise HTTPException(status_code=404, detail='Course not found')
    students = get_students_by_course_id(db, course_id)
    return students
