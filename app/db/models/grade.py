from sqlalchemy import Column, Date, ForeignKey, Integer, SmallInteger
from sqlalchemy.orm import relationship

from db.base_cls import Base


class Grade(Base):
    """Оценка"""

    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    exam_id = Column(Integer, ForeignKey('exams.id'), nullable=False)
    grade_value = Column(SmallInteger, nullable=False)
    date = Column(Date, nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)

    student = relationship('Student', back_populates='grades')
    exam = relationship('Exam', back_populates='grades')
