from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.base_cls import Base


class Exam(Base):
    """Экзамен"""

    __tablename__ = 'exams'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    date_time = Column(DateTime, nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)
    classroom_id = Column(Integer, ForeignKey('classrooms.id'), nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=False)

    course = relationship('Course')
    classroom = relationship('Classroom')
    teacher = relationship('Teacher')
    grades = relationship('Grade')
