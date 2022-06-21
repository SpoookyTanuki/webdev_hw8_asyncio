import asyncio
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import config

engine = create_async_engine(config.PG_DSN_ALC)
Base = declarative_base()


class Contact(Base):

    __tablename__ = 'sw_characters'

    character_id = Column(Integer, primary_key=True)
    birth_year = Column(String(30), nullable=False)
    eye_color = Column(String(30), nullable=False)
    films = Column(String, nullable=False)
    gender = Column(String(20), nullable=False)
    hair_color = Column(String(20), nullable=False)
    height = Column(Float, nullable=False)
    homeworld = Column(String(30), nullable=False)
    mass = Column(Float, nullable=False)
    name = Column(String(50), nullable=True)
    skin_color = Column(String(30), nullable=False)
    species = Column(String, nullable=False)
    starships = Column(String, nullable=False)
    vehicles = Column(String, nullable=False)


async def start_session():

    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    make_async_session = sessionmaker(engine, class_=AsyncSession)

    return make_async_session


async def main():
    await start_session()


if __name__ == '__main__':
    asyncio.run(main())












