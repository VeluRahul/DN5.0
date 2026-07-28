from datetime import timedelta

from fastapi import (
    FastAPI,
    Depends,
    HTTPException,
    status
)

from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import engine
from database import get_db

from models import Base
from models import User

from schemas import (
    UserRegister,
    UserLogin,
    UserResponse,
    Token
)

from security import (
    get_password_hash,
    verify_password,
    create_access_token,
    ACCESS_TOKEN_EXPIRE_MINUTES
)

app = FastAPI(

    title="Course Management API",

    description="JWT Authentication & Security API",

    version="1.0"

)


# -----------------------------
# Create Database Tables
# -----------------------------

@app.on_event("startup")
async def startup():

    async with engine.begin() as conn:

        await conn.run_sync(

            Base.metadata.create_all

        )


# -----------------------------
# CORS Configuration
# -----------------------------

app.add_middleware(

    CORSMiddleware,

    allow_origins=[

        "http://localhost:3000"

    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)


@app.get("/")
async def home():

    return {

        "message":"Authentication API Running"

    }


# --------------------------------------------------
# REGISTER
# --------------------------------------------------

@app.post(

    "/api/v1/auth/register/",

    response_model=UserResponse,

    status_code=status.HTTP_201_CREATED,

    tags=["Authentication"]

)

async def register(

    user: UserRegister,

    db: AsyncSession = Depends(get_db)

):

    result = await db.execute(

        select(User).where(

            User.email == user.email

        )

    )

    existing_user = result.scalar_one_or_none()

    if existing_user:

        raise HTTPException(

            status_code=409,

            detail="Email already registered"

        )

    # Never store plain-text passwords.
    # bcrypt is preferred because it is slow
    # and resistant to brute-force attacks.

    hashed_password = get_password_hash(

        user.password

    )

    new_user = User(

        email=user.email,

        hashed_password=hashed_password,

        is_active=True

    )

    db.add(new_user)

    await db.commit()

    await db.refresh(new_user)

    return new_user


# --------------------------------------------------
# LOGIN
# --------------------------------------------------

@app.post(

    "/api/v1/auth/login/",

    response_model=Token,

    tags=["Authentication"]

)

async def login(

    user: UserLogin,

    db: AsyncSession = Depends(get_db)

):

    result = await db.execute(

        select(User).where(

            User.email == user.email

        )

    )

    db_user = result.scalar_one_or_none()

    if db_user is None:

        raise HTTPException(

            status_code=401,

            detail="Invalid Email or Password"

        )

    if not verify_password(

        user.password,

        db_user.hashed_password

    ):

        raise HTTPException(

            status_code=401,

            detail="Invalid Email or Password"

        )

    access_token = create_access_token(

        data={

            "sub": db_user.email

        },

        expires_delta=timedelta(

            minutes=ACCESS_TOKEN_EXPIRE_MINUTES

        )

    )

    return {

        "access_token": access_token,

        "token_type": "bearer"

    }
  from security import get_current_user

# --------------------------------------------------------
# OAuth2 Authorization Code Flow (Concept)
#
# 1. User logs in through an Authorization Server.
# 2. Authorization Server returns an Authorization Code.
# 3. Client exchanges the code for an Access Token.
# 4. Client uses the Access Token to access protected APIs.
#
# In this hands-on we implemented a simpler JWT login,
# where the client directly receives the JWT after login.
# --------------------------------------------------------


# --------------------------------------------------------
# PROTECTED CREATE COURSE
# --------------------------------------------------------

@app.post(

    "/api/v1/courses/",

    tags=["Courses"]

)

async def create_course(

    course: dict,

    current_user: User = Depends(get_current_user)

):

    return {

        "message": "Course Created Successfully",

        "created_by": current_user.email,

        "course": course

    }


# --------------------------------------------------------
# GET COURSES (Public)
# --------------------------------------------------------

@app.get(

    "/api/v1/courses/",

    tags=["Courses"]

)

async def get_courses():

    return [

        {

            "id": 1,

            "name": "Python",

            "code": "CS301"

        },

        {

            "id": 2,

            "name": "FastAPI",

            "code": "CS302"

        }

    ]


# --------------------------------------------------------
# PROTECTED DELETE COURSE
# --------------------------------------------------------

@app.delete(

    "/api/v1/courses/{course_id}",

    status_code=status.HTTP_204_NO_CONTENT,

    tags=["Courses"]

)

async def delete_course(

    course_id: int,

    current_user: User = Depends(get_current_user)

):

    return


# --------------------------------------------------------
# CURRENT USER
# --------------------------------------------------------

@app.get(

    "/api/v1/auth/me",

    response_model=UserResponse,

    tags=["Authentication"]

)

async def get_me(

    current_user: User = Depends(get_current_user)

):

    return current_user
