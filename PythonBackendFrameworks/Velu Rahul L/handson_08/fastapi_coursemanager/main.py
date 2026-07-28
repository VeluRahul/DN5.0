from typing import Optional

from fastapi import (
    FastAPI,
    Depends,
    HTTPException,
    status,
    Response,
    Request
)

from sqlalchemy import select
from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession

from database import engine
from database import get_db

from models import Base
from models import Course

from schemas import (
    CourseCreate,
    CourseUpdate,
    CourseResponse
)


app = FastAPI(

    title="Course Management API",

    description="RESTful API Design Best Practices",

    version="1.0"

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

        "message":"Course Management API Running"

    }


# -----------------------------------
# CREATE COURSE
# -----------------------------------

@app.post(

    "/api/v1/courses/",

    response_model=CourseResponse,

    status_code=status.HTTP_201_CREATED,

    tags=["Courses"],

    summary="Create Course"

)

async def create_course(

    course: CourseCreate,

    response: Response,

    db: AsyncSession = Depends(get_db)

):

    new_course = Course(

        name=course.name,

        code=course.code,

        credits=course.credits,

        department_id=course.department_id

    )

    db.add(new_course)

    await db.commit()

    await db.refresh(new_course)

    response.headers["Location"] = (

        f"/api/v1/courses/{new_course.id}/"

    )

    return new_course


# -----------------------------------
# GET ALL COURSES
# -----------------------------------

@app.get(

    "/api/v1/courses/",

    tags=["Courses"]

)

async def get_courses(

    request: Request,

    page: int = 1,

    page_size: int = 10,

    search: Optional[str] = None,

    db: AsyncSession = Depends(get_db)

):

    query = select(Course)

    count_query = select(

        func.count()

    ).select_from(Course)

    if search:

        query = query.where(

            Course.name.ilike(f"%{search}%")

            |

            Course.code.ilike(f"%{search}%")

        )

        count_query = count_query.where(

            Course.name.ilike(f"%{search}%")

            |

            Course.code.ilike(f"%{search}%")

        )

    total = (

        await db.execute(count_query)

    ).scalar()

    offset = (page - 1) * page_size

    query = (

        query.offset(offset)

        .limit(page_size)

    )

    result = await db.execute(query)

    courses = result.scalars().all()

    next_url = None

    previous_url = None

    if offset + page_size < total:

        next_url = (

            f"{request.url.path}"

            f"?page={page+1}"

            f"&page_size={page_size}"

        )

    if page > 1:

        previous_url = (

            f"{request.url.path}"

            f"?page={page-1}"

            f"&page_size={page_size}"

        )

    return {

        "count": total,

        "next": next_url,

        "previous": previous_url,

        "results": courses

    }


# -----------------------------------
# GET COURSE
# -----------------------------------

@app.get(

    "/api/v1/courses/{course_id}",

    response_model=CourseResponse,

    tags=["Courses"]

)

async def get_course(

    course_id: int,

    db: AsyncSession = Depends(get_db)

):

    result = await db.execute(

        select(Course).where(

            Course.id == course_id

        )

    )

    course = result.scalar_one_or_none()

    if course is None:

        raise HTTPException(

            status_code=404,

            detail={

                "error":{

                    "code":"NOT_FOUND",

                    "message":f"Course with id {course_id} does not exist",

                    "field":None

                }

            }

        )

    return course

# -----------------------------------
# PUT COURSE
# -----------------------------------

@app.put(

    "/api/v1/courses/{course_id}",

    response_model=CourseResponse,

    tags=["Courses"]

)

async def update_course(

    course_id: int,

    course_data: CourseCreate,

    db: AsyncSession = Depends(get_db)

):

    result = await db.execute(

        select(Course).where(

            Course.id == course_id

        )

    )

    course = result.scalar_one_or_none()

    if course is None:

        raise HTTPException(

            status_code=404,

            detail={

                "error":{

                    "code":"NOT_FOUND",

                    "message":f"Course with id {course_id} does not exist",

                    "field":None

                }

            }

        )

    course.name = course_data.name
    course.code = course_data.code
    course.credits = course_data.credits
    course.department_id = course_data.department_id

    await db.commit()

    await db.refresh(course)

    return course


# -----------------------------------
# PATCH COURSE
# -----------------------------------

@app.patch(

    "/api/v1/courses/{course_id}",

    response_model=CourseResponse,

    tags=["Courses"]

)

async def patch_course(

    course_id: int,

    course_data: CourseUpdate,

    db: AsyncSession = Depends(get_db)

):

    result = await db.execute(

        select(Course).where(

            Course.id == course_id

        )

    )

    course = result.scalar_one_or_none()

    if course is None:

        raise HTTPException(

            status_code=404,

            detail={

                "error":{

                    "code":"NOT_FOUND",

                    "message":f"Course with id {course_id} does not exist",

                    "field":None

                }

            }

        )

    update_data = course_data.model_dump(

        exclude_unset=True

    )

    for key, value in update_data.items():

        setattr(course, key, value)

    await db.commit()

    await db.refresh(course)

    return course


# -----------------------------------
# DELETE COURSE
# -----------------------------------

@app.delete(

    "/api/v1/courses/{course_id}",

    status_code=status.HTTP_204_NO_CONTENT,

    tags=["Courses"]

)

async def delete_course(

    course_id: int,

    db: AsyncSession = Depends(get_db)

):

    result = await db.execute(

        select(Course).where(

            Course.id == course_id

        )

    )

    course = result.scalar_one_or_none()

    if course is None:

        raise HTTPException(

            status_code=404,

            detail={

                "error":{

                    "code":"NOT_FOUND",

                    "message":f"Course with id {course_id} does not exist",

                    "field":None

                }

            }

        )

    await db.delete(course)

    await db.commit()

    return Response(

        status_code=status.HTTP_204_NO_CONTENT

    )


# -----------------------------------
# VALIDATION ERROR HANDLER
# -----------------------------------

from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


@app.exception_handler(RequestValidationError)

async def validation_exception_handler(

    request,

    exc

):

    return JSONResponse(

        status_code=422,

        content={

            "error":{

                "code":"VALIDATION_ERROR",

                "message":"Validation Failed",

                "field":str(exc)

            }

        }

    )


# -----------------------------------
# GENERIC HTTP ERROR HANDLER
# -----------------------------------

@app.exception_handler(HTTPException)

async def http_exception_handler(

    request,

    exc

):

    if isinstance(exc.detail, dict):

        return JSONResponse(

            status_code=exc.status_code,

            content=exc.detail

        )

    return JSONResponse(

        status_code=exc.status_code,

        content={

            "error":{

                "code":"HTTP_ERROR",

                "message":exc.detail,

                "field":None

            }

        }

    )
