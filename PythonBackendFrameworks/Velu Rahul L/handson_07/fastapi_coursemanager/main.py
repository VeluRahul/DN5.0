from typing import Optional

from fastapi import FastAPI
from fastapi import Depends
from fastapi import HTTPException
from fastapi import BackgroundTasks
from fastapi import status

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from database import engine

from models import Base
from models import Course

from schemas import CourseCreate
from schemas import CourseUpdate
from schemas import CourseResponse

app = FastAPI(

    title="Course Management API",

    description="FastAPI CRUD API for Digital Nurture 5.0",

    version="1.0",

    contact={

        "name":"Velu Rahul L",

        "email":"rahul@example.com"

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


@app.post(

    "/api/courses/",

    response_model=CourseResponse,

    status_code=status.HTTP_201_CREATED,

    tags=["Courses"],

    summary="Create Course",

    response_description="Created Course"

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
