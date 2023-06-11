from sqlalchemy import Boolean, Column, Date, Integer, SmallInteger, String

from db.base_cls import Base


class Semester(Base):
    """Семестр"""

    __tablename__ = 'semesters'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    is_current = Column(Boolean, default=False, nullable=False)
    year = Column(SmallInteger, nullable=False)
