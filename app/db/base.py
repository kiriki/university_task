from .base_cls import Base  # noqa F401
from .models.assignment import Assignment  # noqa F401
from .models.building import Building  # noqa F401
from .models.classroom import Classroom  # noqa F401
from .models.course import Course  # noqa F401
from .models.course_program import CourseProgram  # noqa F401
from .models.department import Department  # noqa F401
from .models.exam import Exam  # noqa F401
from .models.faculty import Faculty  # noqa F401
from .models.grade import Grade  # noqa F401
from .models.group import Group  # noqa F401
from .models.schedule import Schedule  # noqa F401
from .models.semester import Semester  # noqa F401
from .models.student import Student  # noqa F401
from .models.study_plan import StudyPlan  # noqa F401
from .models.teacher import Teacher  # noqa F401

# imports is required to populate the Base.metadata
#  before being imported by Alembic
