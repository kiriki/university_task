from fastapi import HTTPException
from sqlalchemy.orm import Session

from db.models.course import Course as CourseModel
from schemas.course import CourseCreate


def get_department(db: Session, department_id: int):
    return db.query(CourseModel).filter(CourseModel.department_id == department_id).first()


def create_course_repo(db: Session, course: CourseCreate):
    if not get_department(db, course.department_id):
        raise HTTPException(status_code=404, detail='Department not found')

    new_course = CourseModel(**course.dict())
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course


def get_course_by_id(db: Session, course_id: int):
    return db.query(CourseModel).filter(CourseModel.id == course_id).first()


def get_students_by_course_id(db: Session, course_id: int):
    # todo filter students by course_id
    return None
