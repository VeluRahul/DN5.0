from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import Date


class Base(DeclarativeBase):
    pass


class Department(Base):

    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(100)
    )

    head_of_dept: Mapped[str] = mapped_column(
        String(100)
    )

    budget: Mapped[float]

    courses = relationship(
        "Course",
        back_populates="department"
    )


class Course(Base):

    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(100)
    )

    code: Mapped[str] = mapped_column(
        String(20),
        unique=True
    )

    credits: Mapped[int]

    department_id: Mapped[int] = mapped_column(
        ForeignKey("departments.id")
    )

    department = relationship(
        "Department",
        back_populates="courses"
    )

    enrollments = relationship(
        "Enrollment",
        back_populates="course"
    )


class Student(Base):

    __tablename__ = "students"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    first_name: Mapped[str] = mapped_column(
        String(100)
    )

    last_name: Mapped[str] = mapped_column(
        String(100)
    )

    email: Mapped[str] = mapped_column(
        String(100),
        unique=True
    )

    department_id: Mapped[int] = mapped_column(
        ForeignKey("departments.id")
    )

    enrollment_year: Mapped[int]

    enrollments = relationship(
        "Enrollment",
        back_populates="student"
    )


class Enrollment(Base):

    __tablename__ = "enrollments"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    student_id: Mapped[int] = mapped_column(
        ForeignKey("students.id")
    )

    course_id: Mapped[int] = mapped_column(
        ForeignKey("courses.id")
    )

    enrollment_date: Mapped[Date]

    grade: Mapped[str] = mapped_column(
        String(2),
        nullable=True
    )

    student = relationship(
        "Student",
        back_populates="enrollments"
    )

    course = relationship(
        "Course",
        back_populates="enrollments"
    )
