from typing import Optional

from fastapi import FastAPI
from fastapi import Depends
from fastapi import HTTPException
from fastapi import BackgroundTasks
from fastapi import status

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import engine
from database import get_db

from models import Base
from models import Course
from models import Student
from models import Enrollment

from schemas import CourseCreate
from schemas import CourseUpdate
from schemas import CourseResponse

app = FastAPI(

    title="Course Management API",

    description="Course Management API using FastAPI",

    version="1.0",

    contact={
        "name":"Velu Rahul L",
        "email":"admin@college.edu"
    }

)


@app.on_event("startup")
async def startup():

    async with engine.begin() as conn:

        await conn.run_sync(

            Base.metadata.create_all

        )


@app.get("/")

async def home():

    return {

        "message":"API Running"

    }


# ----------------------------------------
# CREATE COURSE
# ----------------------------------------

@app.post(

    "/api/courses/",

    response_model=CourseResponse,

    status_code=status.HTTP_201_CREATED,

    tags=["Courses"],

    summary="Create Course",

    response_description="Returns Newly Created Course"

)

async def create_course(

    course:CourseCreate,

    db:AsyncSession=Depends(get_db)

):

    new_course=Course(

        name=course.name,

        code=course.code,

        credits=course.credits,

        department_id=course.department_id

    )

    db.add(new_course)

    await db.commit()

    await db.refresh(new_course)

    return new_course


# ----------------------------------------
# GET ALL COURSES
# ----------------------------------------

@app.get(

    "/api/courses/",

    response_model=list[CourseResponse],

    tags=["Courses"]

)

async def get_courses(

    skip:int=0,

    limit:int=10,

    department_id:Optional[int]=None,

    db:AsyncSession=Depends(get_db)

):

    query=select(Course)

    if department_id is not None:

        query=query.where(

            Course.department_id==department_id

        )

    query=query.offset(skip).limit(limit)

    result=await db.execute(query)

    courses=result.scalars().all()

    return courses


# ----------------------------------------
# GET COURSE BY ID
# ----------------------------------------

@app.get(

    "/api/courses/{course_id}",

    response_model=CourseResponse,

    tags=["Courses"]

)

async def get_course(

    course_id:int,

    db:AsyncSession=Depends(get_db)

):

    result=await db.execute(

        select(Course).where(

            Course.id==course_id

        )

    )

    course=result.scalar_one_or_none()

    if course is None:

        raise HTTPException(

            status_code=404,

            detail="Course not found"

        )

    return course


# ----------------------------------------
# UPDATE COURSE
# ----------------------------------------

@app.put(

    "/api/courses/{course_id}",

    response_model=CourseResponse,

    tags=["Courses"]

)

async def update_course(

    course_id:int,

    course_data:CourseUpdate,

    db:AsyncSession=Depends(get_db)

):

    result=await db.execute(

        select(Course).where(

            Course.id==course_id

        )

    )

    course=result.scalar_one_or_none()

    if course is None:

        raise HTTPException(

            status_code=404,

            detail="Course not found"

        )

    update_data=course_data.model_dump(

        exclude_unset=True

    )

    for key,value in update_data.items():

        setattr(

            course,

            key,

            value

        )

    await db.commit()

    await db.refresh(course)

    return course


# ----------------------------------------
# DELETE COURSE
# ----------------------------------------

@app.delete(

    "/api/courses/{course_id}",

    status_code=status.HTTP_204_NO_CONTENT,

    tags=["Courses"]

)

async def delete_course(

    course_id:int,

    db:AsyncSession=Depends(get_db)

):

    result=await db.execute(

        select(Course).where(

            Course.id==course_id

        )

    )

    course=result.scalar_one_or_none()

    if course is None:

        raise HTTPException(

            status_code=404,

            detail="Course not found"

        )

    await db.delete(course)

    await db.commit()

# ----------------------------------------
# BACKGROUND TASK
# ----------------------------------------

def send_confirmation_email(student_email: str):

    print(f"Sending confirmation to {student_email}")


# ----------------------------------------
# CREATE STUDENT
# ----------------------------------------

@app.post(

    "/api/students/",

    response_model=StudentResponse,

    status_code=status.HTTP_201_CREATED,

    tags=["Students"]

)

async def create_student(

    student: StudentCreate,

    db: AsyncSession = Depends(get_db)

):

    new_student = Student(

        first_name=student.first_name,

        last_name=student.last_name,

        email=student.email,

        department_id=student.department_id,

        enrollment_year=student.enrollment_year

    )

    db.add(new_student)

    await db.commit()

    await db.refresh(new_student)

    return new_student


# ----------------------------------------
# GET ALL STUDENTS
# ----------------------------------------

@app.get(

    "/api/students/",

    response_model=list[StudentResponse],

    tags=["Students"]

)

async def get_students(

    db: AsyncSession = Depends(get_db)

):

    result = await db.execute(

        select(Student)

    )

    return result.scalars().all()


# ----------------------------------------
# CREATE ENROLLMENT
# ----------------------------------------

@app.post(

    "/api/enrollments/",

    response_model=EnrollmentResponse,

    status_code=status.HTTP_201_CREATED,

    tags=["Enrollments"],

    summary="Create Enrollment",

    response_description="Enrollment Created Successfully"

)

async def create_enrollment(

    enrollment: EnrollmentCreate,

    background_tasks: BackgroundTasks,

    db: AsyncSession = Depends(get_db)

):

    new_enrollment = Enrollment(

        student_id=enrollment.student_id,

        course_id=enrollment.course_id,

        enrollment_date=enrollment.enrollment_date,

        grade=enrollment.grade

    )

    db.add(new_enrollment)

    await db.commit()

    await db.refresh(new_enrollment)

    student = await db.get(

        Student,

        enrollment.student_id

    )

    if student:

        background_tasks.add_task(

            send_confirmation_email,

            student.email

        )

    return new_enrollment


# ----------------------------------------
# GET ALL ENROLLMENTS
# ----------------------------------------

@app.get(

    "/api/enrollments/",

    response_model=list[EnrollmentResponse],

    tags=["Enrollments"]

)

async def get_enrollments(

    db: AsyncSession = Depends(get_db)

):

    result = await db.execute(

        select(Enrollment)

    )

    return result.scalars().all()


# ----------------------------------------
# STUDENTS OF A COURSE
# ----------------------------------------

@app.get(

    "/api/courses/{course_id}/students/",

    tags=["Courses"],

    summary="Students Enrolled in a Course"

)

async def get_course_students(

    course_id: int,

    db: AsyncSession = Depends(get_db)

):

    result = await db.execute(

        select(Student)

        .join(

            Enrollment,

            Student.id == Enrollment.student_id

        )

        .where(

            Enrollment.course_id == course_id

        )

    )

    return result.scalars().all()
