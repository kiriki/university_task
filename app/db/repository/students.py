from fastapi import HTTPException
from sqlalchemy.orm import Session

from db.models.group import Group as GroupModel
from db.models.student import Student as StudentDb
from schemas.student import StudentCreate, StudentUpdate


def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(StudentDb).offset(skip).limit(limit).all()


def get_student(db: Session, student_id: int):
    return db.query(StudentDb).filter(StudentDb.id == student_id).first()


def get_group(db: Session, group_id: int):
    return db.query(GroupModel).filter(GroupModel.id == group_id).first()


def create_student_repo(db: Session, student: StudentCreate):
    if not get_group(db, student.group_id):
        raise HTTPException(status_code=404, detail='Group not found')

    new_student = StudentDb(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


def update_student_repo(student_id: int, student: StudentUpdate, db: Session):
    existing_student = db.query(StudentDb).filter(StudentDb.id == student_id).first()
    if existing_student:
        for field, value in student.dict(exclude_unset=True).items():
            setattr(existing_student, field, value)
        db.commit()
        db.refresh(existing_student)
        return existing_student
    return None


def delete_student_repo(student_id: int, db: Session):
    existing_student = db.query(StudentDb).filter(StudentDb.id == student_id).first()
    if existing_student:
        db.delete(existing_student)
        db.commit()
        return True
    return False
