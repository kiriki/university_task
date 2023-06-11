from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.repository.teachers import get_teachers
from db.session import get_db
from schemas.teacher import Teacher

router = APIRouter(
    responses={404: {'description': 'Not found'}},
)


# GET /teachers - получить список всех преподавателей.


@router.get('/', description='Get all teachers', response_model=list[Teacher])
def read_teachers(db: Session = Depends(get_db)) -> list[Teacher]:
    return get_teachers(db)
