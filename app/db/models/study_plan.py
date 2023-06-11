from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from db.base_cls import Base


class StudyPlan(Base):
    """Учебный план"""

    __tablename__ = 'study_plans'

    id = Column(Integer, primary_key=True, index=True)
    schedule_id = Column(Integer, ForeignKey('schedules.id'))
    schedule = relationship('Schedule')
