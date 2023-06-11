from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.base_cls import Base


class Department(Base):
    """Отделение"""

    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    faculty_id = Column(Integer, ForeignKey('faculties.id'), nullable=False)

    faculty = relationship('Faculty', back_populates='departments')
    groups = relationship('Group', back_populates='department')
