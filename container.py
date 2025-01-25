from dependency_injector import containers, providers
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from src.service.schedule.schedule_service_impl import ScheduleServiceImpl
from src.repository.schedule.schedule_repository_impl import ScheduleRepositoryImpl
from src.repository.user import UserRepositoryImpl
from src.service.user import UserServiceImpl
from src.common.function.jwt import *
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "mysql+aiomysql://diary_db:bank_db@localhost:3306/diary_db"

Base = declarative_base()


class AppContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=["src.controller"],
        modules=[__name__],
    )

    # Async Database Engine
    engine: providers.Singleton[AsyncEngine] = providers.Singleton(
        create_async_engine, DATABASE_URL, echo=True  # SQLAlchemy 로깅 (선택)
    )

    # Async Session Factory
    session_factory: providers.Factory[sessionmaker] = providers.Factory(
        sessionmaker, bind=engine, class_=AsyncSession, expire_on_commit=False
    )

    async_session = providers.Resource(
        lambda session_factory: session_factory(), session_factory=session_factory
    )

    jwt_encoder = providers.Singleton(JWTEncoder)
    jwt_decoder = providers.Singleton(JWTDecoder)
    user_repository = providers.Factory(UserRepositoryImpl, session=async_session)
    schedule_repository = providers.Factory(
        ScheduleRepositoryImpl, session=async_session
    )
    user_service = providers.Factory(
        UserServiceImpl,
        user_repository=user_repository,
        jwt_encoder=jwt_encoder,
        jwt_decoder=jwt_decoder,
    )
    schedule_service = providers.Factory(
        ScheduleServiceImpl, schedule_repository=schedule_repository
    )
