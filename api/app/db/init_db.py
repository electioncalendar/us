from sqlalchemy.orm import Session

from .. import crud, schemas
from ..conf import settings
from . import base  # noqa: F401

# make sure all SQL Alchemy models are imported (api.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)

    user = crud.get_user_by_email(db, email=settings.SUPERUSER_EMAIL)
    if not user:
        user_in = schemas.UserCreate(
            email=settings.SUPERUSER_EMAIL,
            password=settings.SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = crud.create_user(db, user=user_in)
