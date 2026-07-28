from app import db


class Department(db.Model):

    __tablename__ = "departments"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    head_of_dept = db.Column(
        db.String(100)
    )

    budget = db.Column(
        db.Float
    )

    courses = db.relationship(
        "Course",
        back_populates="department"
    )


class Course(db.Model):

    __tablename__ = "courses"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    code = db.Column(
        db.String(20),
        unique=True
    )

    credits = db.Column(
        db.Integer
    )

    department_id = db.Column(
        db.Integer,
        db.ForeignKey("departments.id")
    )

    department = db.relationship(
        "Department",
        back_populates="courses"
    )


class Student(db.Model):

    __tablename__ = "students"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    first_name = db.Column(
        db.String(100)
    )

    last_name = db.Column(
        db.String(100)
    )

    email = db.Column(
        db.String(100),
        unique=True
    )

    department_id = db.Column(
        db.Integer,
        db.ForeignKey("departments.id")
    )

    enrollment_year = db.Column(
        db.Integer
    )


class Enrollment(db.Model):

    __tablename__ = "enrollments"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    student_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id")
    )

    course_id = db.Column(
        db.Integer,
        db.ForeignKey("courses.id")
    )

    enrollment_date = db.Column(
        db.Date
    )

    grade = db.Column(
        db.String(2)
    )

    student = db.relationship("Student")

    course = db.relationship("Course")
