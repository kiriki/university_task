from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db.base_cls import Base


class Building(Base):
    """Здание"""

    __tablename__ = 'buildings'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    address = Column(String(200), nullable=False)
    floors = Column(Integer, nullable=False)
    description = Column(String, nullable=False)

    classrooms = relationship('Classroom', back_populates='building')
