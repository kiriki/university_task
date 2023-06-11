from sqlalchemy.orm import Session

from db.models.teacher import Teacher as TeacherModel


def get_teachers(db: Session):
    return db.query(TeacherModel).all()
