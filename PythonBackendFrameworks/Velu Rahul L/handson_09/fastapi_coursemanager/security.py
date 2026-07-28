from datetime import datetime
from datetime import timedelta
from datetime import timezone

from jose import JWTError
from jose import jwt

from passlib.context import CryptContext

from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from fastapi.security import OAuth2PasswordBearer

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from models import User


SECRET_KEY = "DigitalNurtureFastAPISecretKey"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30


pwd_context = CryptContext(

    schemes=["bcrypt"],

    deprecated="auto"

)


oauth2_scheme = OAuth2PasswordBearer(

    tokenUrl="/api/v1/auth/login"

)


# ----------------------------------------------------
# Password Hashing
# bcrypt is intentionally slow and secure.
# Never use MD5 or SHA256 for password storage.
# ----------------------------------------------------

def get_password_hash(password: str):

    return pwd_context.hash(password)


def verify_password(

    plain_password,

    hashed_password

):

    return pwd_context.verify(

        plain_password,

        hashed_password

    )


# ----------------------------------------------------
# JWT Creation
# ----------------------------------------------------

def create_access_token(

    data: dict,

    expires_delta: timedelta | None = None

):

    to_encode = data.copy()

    if expires_delta:

        expire = (

            datetime.now(timezone.utc)

            + expires_delta

        )

    else:

        expire = (

            datetime.now(timezone.utc)

            + timedelta(

                minutes=ACCESS_TOKEN_EXPIRE_MINUTES

            )

        )

    to_encode.update(

        {

            "exp": expire

        }

    )

    return jwt.encode(

        to_encode,

        SECRET_KEY,

        algorithm=ALGORITHM

    )


# ----------------------------------------------------
# Current User Dependency
# ----------------------------------------------------

async def get_current_user(

    token: str = Depends(oauth2_scheme),

    db: AsyncSession = Depends(get_db)

):

    credentials_exception = HTTPException(

        status_code=status.HTTP_401_UNAUTHORIZED,

        detail="Invalid or Expired Token",

        headers={

            "WWW-Authenticate": "Bearer"

        }

    )

    try:

        payload = jwt.decode(

            token,

            SECRET_KEY,

            algorithms=[ALGORITHM]

        )

        email = payload.get("sub")

        if email is None:

            raise credentials_exception

    except JWTError:

        raise credentials_exception

    result = await db.execute(

        select(User).where(

            User.email == email

        )

    )

    user = result.scalar_one_or_none()

    if user is None:

        raise credentials_exception

    return user
