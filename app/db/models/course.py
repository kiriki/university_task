from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import mapped_column, relationship

from db.base_cls import Base


class Course(Base):
    """Курс"""

    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    duration_weeks = Column(Integer, nullable=False)
    teacher_id = mapped_column(ForeignKey('teachers.id'), nullable=False)
    department_id = mapped_column(ForeignKey('departments.id'), nullable=False)

    department = relationship('Department')
    teacher = relationship('Teacher')
