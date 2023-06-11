from sqlalchemy.orm import Session

from db.models.grade import Grade as GradeDb
from schemas.grade import GradeCreate, GradeUpdate


def get_grade(db: Session, grade_id: int) -> GradeDb | None:
    return db.query(GradeDb).filter(GradeDb.id == grade_id).first()


def create_grade_repo(db: Session, grade: GradeCreate) -> GradeDb:
    # todo check if student, course and exam exists
    new_grade = GradeDb(**grade.dict())
    db.add(new_grade)
    db.commit()
    db.refresh(new_grade)
    return new_grade


def update_grade_repo(existing_grade: GradeDb, grade: GradeUpdate, db: Session) -> GradeDb:
    existing_grade.grade_value = grade.grade_value
    existing_grade.date = grade.date
    db.commit()
    db.refresh(existing_grade)

    return existing_grade
