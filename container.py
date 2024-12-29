from dependency_injector import containers, providers
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from src.repository.user import UserRepositoryImpl
from src.service.user import UserServiceImpl
DATABASE_URL = "mysql+aiomysql://diary_db:bank_db@localhost:3306/diary_db"

class AppContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["src.controller", "src.service", "src.repository"])
    
    # Async Database Engine
    engine: providers.Singleton[AsyncEngine] = providers.Singleton(
        create_async_engine,
        DATABASE_URL,
        echo=True  # SQLAlchemy 로깅 (선택)
    )
    
    # Async Session Factory
    session_factory: providers.Factory[sessionmaker] = providers.Factory(
        sessionmaker,
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False
    )    
    
    async_session = providers.Resource(
        lambda session_factory: session_factory(),
        session_factory = session_factory
    )

    user_repository = providers.Factory(
        UserRepositoryImpl,
        session = async_session
    )
    
    user_service = providers.Factory(
        UserServiceImpl,
        user_repository
    )