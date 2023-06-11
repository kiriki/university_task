from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.base_cls import Base


class Group(Base):
    """Группа"""

    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    department_id = Column(Integer, ForeignKey('departments.id'))
    department = relationship('Department', back_populates='groups')
    students = relationship('Student', back_populates='group')
