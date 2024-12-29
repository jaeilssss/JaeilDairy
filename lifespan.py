from contextlib import asynccontextmanager
from fastapi import FastAPI
from container import AppContainer
from sqlalchemy import text
container = AppContainer()
# container.wire(modules=["__main__"])
@asynccontextmanager
async def life_span(app: FastAPI):
    async with container.engine().connect() as connection:
        await connection.execute(text("SELECT 1"))  # 연결 확인용 쿼리
        print("Database connection initialized")

    try:
        yield  # 애플리케이션 실행 (요청 처리)
    finally:
        # 애플리케이션 종료 시 실행
        await container.engine().dispose()
        print("Database connection disposed")