from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db.base_cls import Base


class Faculty(Base):
    """Факультет"""

    __tablename__ = 'faculties'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    address = Column(String(200), nullable=False)
    phone = Column(String(20), nullable=False)
    email = Column(String, nullable=False)
    description = Column(String, nullable=False)

    departments = relationship('Department', back_populates='faculty')
