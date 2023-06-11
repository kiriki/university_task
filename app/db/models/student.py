from enum import Enum as PyEnum

from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.base_cls import Base


class GenderEnum(PyEnum):
    male = 'M'
    female = 'F'


class Student(Base):
    """Студент"""

    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)
    gender = Column(String(length=1), nullable=False)
    phone = Column(String, nullable=False)
    admission_date = Column(Date, nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id'), nullable=False)

    group = relationship('Group', back_populates='students')
    grades = relationship('Grade', back_populates='student')
    assignments = relationship('Assignment', back_populates='student')
