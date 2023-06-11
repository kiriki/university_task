from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

from db.base_cls import Base


class CourseProgram(Base):
    """Программа курса на определённый семестр"""

    __tablename__ = 'course_programs'

    id = Column(Integer, primary_key=True, index=True)
    description = Column(Text, nullable=False)
    hours = Column(Integer, nullable=False)  # кол-во учебных часов
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)
    semester_id = Column(Integer, ForeignKey('semesters.id'), nullable=False)

    course = relationship('Course')
    semester = relationship('Semester')
