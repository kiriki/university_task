from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.base_cls import Base


class Classroom(Base):
    """Аудитория"""

    __tablename__ = 'classrooms'

    id = Column(Integer, primary_key=True, index=True)
    room_number = Column(String(50), nullable=False)
    capacity = Column(Integer, nullable=False)
    room_type = Column(String(100), nullable=False)
    floor = Column(Integer, nullable=False)
    building_id = Column(Integer, ForeignKey('buildings.id'), nullable=False)

    building = relationship('Building', back_populates='classrooms')
