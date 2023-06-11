from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.repository.students import create_student_repo, delete_student_repo, get_student, update_student_repo
from db.session import get_db
from schemas.student import Student, StudentCreate, StudentUpdate

router = APIRouter(
    responses={404: {'description': 'Not found'}},
)


# POST /students - создать нового студента.
# GET /students/{student_id} - получить информацию о студенте по его id.
# PUT /students/{student_id} - обновить информацию о студенте по его id.
# DELETE /students/{student_id} - удалить студента по его id.


@router.post('/', description='Create a new student', response_model=Student)
def create_student(stud: StudentCreate, db: Session = Depends(get_db)) -> Student:
    return create_student_repo(db, stud)


@router.get('/{student_id:int}', description='Get information about a student by its ID', response_model=Student)
def read_student(student_id: int, db: Session = Depends(get_db)) -> Student:
    db_student = get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail='Student not found')
    return db_student


@router.put('/{student_id:int}', description='Update information about a student by its ID', response_model=Student)
def update_student(student_id: int, stud: StudentUpdate, db: Session = Depends(get_db)) -> Student:
    return update_student_repo(student_id, stud, db)


@router.delete('/{student_id:int}', description='Delete a student by its ID')
def delete_student(student_id: int, db: Session = Depends(get_db)) -> dict:
    rest = delete_student_repo(student_id, db)
    if not rest:
        raise HTTPException(status_code=404, detail='Student not found')
    return {'msg': 'Successfully deleted.'}
