from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.repository.grades import create_grade_repo, get_grade, update_grade_repo
from db.session import get_db
from schemas.grade import Grade, GradeCreate, GradeUpdate

router = APIRouter(
    responses={404: {'description': 'Not found'}},
)


@router.post('/', description='Create a new grade for a student in the course', response_model=Grade)
def create_grade(grade: GradeCreate, db: Session = Depends(get_db)) -> Grade:
    return create_grade_repo(db, grade)


@router.put('/{grade_id:int}', description='Update a grade for a student in the course', response_model=Grade)
def update_grade(grade_id: int, grade: GradeUpdate, db: Session = Depends(get_db)) -> Grade:
    existing_grade = get_grade(db=db, grade_id=grade_id)
    if existing_grade is None:
        raise HTTPException(status_code=404, detail='Grade not found')

    return update_grade_repo(existing_grade, grade, db)
