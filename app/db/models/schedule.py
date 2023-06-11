from sqlalchemy import Column, Date, ForeignKey, Integer
from sqlalchemy.orm import relationship

from db.base_cls import Base


class Schedule(Base):
    """Расписание курса по программе для группы"""

    __tablename__ = 'schedules'

    id = Column(Integer, primary_key=True)

    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id'), nullable=False)
    course_program_id = Column(Integer, ForeignKey('course_programs.id'), nullable=False)

    course_program = relationship('CourseProgram')
    group = relationship('Group')
