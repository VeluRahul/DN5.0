"""
Topic :
CRUD Operations using SQLAlchemy ORM

"""

from datetime import date

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import (
    Base,
    Department,
    Student,
    Course,
    Enrollment,
    Professor
)

# =====================================================
# Database Connection
# =====================================================

DATABASE_URL = "mysql+mysqlconnector://root:password@localhost/college_db_orm"

engine = create_engine(
    DATABASE_URL,
    echo=True
)

Session = sessionmaker(bind=engine)

session = Session()

# =====================================================
# TASK 81
# Insert Departments
# =====================================================

cs = Department(
    dept_name="Computer Science",
    head_of_dept="Dr. Ramesh Kumar",
    budget=850000
)

ec = Department(
    dept_name="Electronics",
    head_of_dept="Dr. Priya Nair",
    budget=620000
)

me = Department(
    dept_name="Mechanical",
    head_of_dept="Dr. Suresh Iyer",
    budget=540000
)

session.add_all([cs, ec, me])

session.commit()

print("\nDepartments Inserted Successfully")

# =====================================================
# Insert Students
# =====================================================

s1 = Student(
    first_name="Arjun",
    last_name="Mehta",
    email="arjun@gmail.com",
    enrollment_year=2022,
    department=cs
)

s2 = Student(
    first_name="Priya",
    last_name="Suresh",
    email="priya@gmail.com",
    enrollment_year=2022,
    department=cs
)

s3 = Student(
    first_name="Rahul",
    last_name="Velu",
    email="rahul@gmail.com",
    enrollment_year=2023,
    department=cs
)

s4 = Student(
    first_name="Rohan",
    last_name="Verma",
    email="rohan@gmail.com",
    enrollment_year=2021,
    department=ec
)

s5 = Student(
    first_name="Sneha",
    last_name="Patel",
    email="sneha@gmail.com",
    enrollment_year=2023,
    department=me
)

session.add_all([s1, s2, s3, s4, s5])

session.commit()

print("Students Inserted Successfully")

# =====================================================
# TASK 82
# Insert Courses
# =====================================================

c1 = Course(
    course_name="Data Structures",
    course_code="CS101",
    credits=4,
    department=cs
)

c2 = Course(
    course_name="Database Management",
    course_code="CS102",
    credits=3,
    department=cs
)

c3 = Course(
    course_name="Circuit Theory",
    course_code="EC101",
    credits=3,
    department=ec
)

session.add_all([c1, c2, c3])

session.commit()

print("Courses Inserted Successfully")

# =====================================================
# Insert Enrollments
# =====================================================

e1 = Enrollment(
    student=s1,
    course=c1,
    enrollment_date=date.today(),
    grade="A"
)

e2 = Enrollment(
    student=s2,
    course=c1,
    enrollment_date=date.today(),
    grade="B"
)

e3 = Enrollment(
    student=s3,
    course=c2,
    enrollment_date=date.today(),
    grade="A"
)

e4 = Enrollment(
    student=s4,
    course=c3,
    enrollment_date=date.today(),
    grade="B"
)

session.add_all([e1, e2, e3, e4])

session.commit()

print("Enrollments Inserted Successfully")

# =====================================================
# TASK 83
# Students in Computer Science
# =====================================================

print("\nStudents in Computer Science\n")

students = session.query(Student)\
.join(Department)\
.filter(
Department.dept_name == "Computer Science"
).all()

for student in students:

    print(
        student.first_name,
        student.last_name,
        student.email
    )

# =====================================================
# TASK 84
# Read Enrollments
# =====================================================

print("\nEnrollment Details\n")

enrollments = session.query(
Enrollment
).all()

for enrollment in enrollments:

    print(
        enrollment.student.first_name,
        "->",
        enrollment.course.course_name,
        enrollment.grade
    )

# =====================================================
# TASK 85
# Update Student
# =====================================================

student = session.query(
Student
).filter_by(
email="rahul@gmail.com"
).first()

student.enrollment_year = 2024

session.commit()

print("\nStudent Updated Successfully")

# =====================================================
# TASK 86
# Delete Enrollment
# =====================================================

record = session.query(
Enrollment
).first()

session.delete(record)

session.commit()

print("Enrollment Deleted Successfully")

# =====================================================
# Close Session
# =====================================================

session.close()

print("\nSession Closed")
