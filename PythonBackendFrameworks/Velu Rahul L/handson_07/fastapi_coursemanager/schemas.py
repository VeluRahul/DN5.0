from pydantic import BaseModel
from typing import Optional
from datetime import date


# -----------------------------
# Department Schemas
# -----------------------------

class DepartmentBase(BaseModel):

    name: str

    head_of_dept: str

    budget: float


class DepartmentCreate(DepartmentBase):
    pass


class DepartmentResponse(DepartmentBase):

    id: int

    class Config:
        from_attributes = True


# -----------------------------
# Course Schemas
# -----------------------------

class CourseBase(BaseModel):

    name: str

    code: str

    credits: int

    department_id: int


class CourseCreate(CourseBase):
    pass


class CourseUpdate(BaseModel):

    name: Optional[str] = None

    code: Optional[str] = None

    credits: Optional[int] = None

    department_id: Optional[int] = None


class CourseResponse(CourseBase):

    id: int

    class Config:
        from_attributes = True


# -----------------------------
# Student Schemas
# -----------------------------

class StudentBase(BaseModel):

    first_name: str

    last_name: str

    email: str

    department_id: int

    enrollment_year: int


class StudentCreate(StudentBase):
    pass


class StudentResponse(StudentBase):

    id: int

    class Config:
        from_attributes = True


# -----------------------------
# Enrollment Schemas
# -----------------------------

class EnrollmentBase(BaseModel):

    student_id: int

    course_id: int

    enrollment_date: date

    grade: Optional[str] = None


class EnrollmentCreate(EnrollmentBase):
    pass


class EnrollmentResponse(EnrollmentBase):

    id: int

    class Config:
        from_attributes = True


# -----------------------------
# Nested Response
# -----------------------------

class DepartmentWithCourses(BaseModel):

    id: int

    name: str

    head_of_dept: str

    budget: float

    courses: list[CourseResponse] = []

    class Config:
        from_attributes = True
