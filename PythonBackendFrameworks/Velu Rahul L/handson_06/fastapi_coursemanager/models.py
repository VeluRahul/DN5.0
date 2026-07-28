from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from sqlalchemy import Integer
from sqlalchemy import String


class Base(DeclarativeBase):

    pass


class Course(Base):

    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(100)
    )

    code: Mapped[str] = mapped_column(
        String(20),
        unique=True
    )

    credits: Mapped[int] = mapped_column(
        Integer
    )

    department_id: Mapped[int] = mapped_column(
        Integer
    )
