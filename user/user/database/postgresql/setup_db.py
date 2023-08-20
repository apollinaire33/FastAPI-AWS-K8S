from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from user.core.config import database_url

Base = declarative_base()

engine = create_async_engine(database_url, echo=True)

async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_db() -> None:
    async with async_session() as session:
        yield session
