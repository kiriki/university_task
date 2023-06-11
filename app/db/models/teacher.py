from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import mapped_column, relationship

from db.base_cls import Base


class Teacher(Base):
    """Преподаватель"""

    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    birth_date = Column(Date, nullable=False)
    gender = Column(String(length=1), nullable=False)
    phone = Column(String(20), nullable=False)
    class_room_id = Column(Integer, ForeignKey('classrooms.id'))
    department_id = mapped_column(ForeignKey('departments.id'), nullable=False)

    class_room = relationship('Classroom')
    department = relationship('Department')
    assignments = relationship('Assignment')
