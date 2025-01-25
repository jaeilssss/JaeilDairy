from contextlib import asynccontextmanager
from fastapi import FastAPI
from container import AppContainer
from sqlalchemy import text
from sqlalchemy.ext.declarative import declarative_base

container = AppContainer()
container.wire(modules=["__main__"])


@asynccontextmanager
async def life_span(app: FastAPI):
    app.container = container
    async with container.engine().connect() as connection:
        await connection.execute(text("SELECT 1"))  # 연결 확인용 쿼리
        # 모든 모델 선언 후 실행
        print("Database connection initialized")

    try:
        yield  # 애플리케이션 실행 (요청 처리)
    finally:
        # 애플리케이션 종료 시 실행
        await container.engine().dispose()
        print("Database connection disposed")
