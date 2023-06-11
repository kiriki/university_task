from sqlalchemy import Column, Date, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from db.base_cls import Base


class Assignment(Base):
    """Задание для самостоятельной работы"""

    __tablename__ = 'assignments'

    id = Column(Integer, primary_key=True, index=True)
    assignment_name = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    issue_date = Column(Date, nullable=False)
    due_date = Column(Date, nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=False)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)

    course = relationship('Course')
    teacher = relationship('Teacher', back_populates='assignments')
    student = relationship('Student', back_populates='assignments')
