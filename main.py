from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from src.common.middleware.blacklist import blacklist_middleware
from src.controller.schedule_router import schedule_router
from src.controller.user_router import user_router
from src.common.exception.exception import BaseExceptionHanlder
from lifespan import life_span
import sys
import os

app = FastAPI(lifespan=life_span)
app.include_router(router=user_router, prefix="/user", tags=["유저 API"])
app.include_router(router=schedule_router, prefix="/schedule", tags=["일정관리 API"])

app.middleware("http")(blacklist_middleware)

load_dotenv()
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))


@app.exception_handler(BaseExceptionHanlder)
async def base_exception_handler(request: Request, exc: BaseExceptionHanlder):
    return JSONResponse(
        status_code=exc.status_code, content={"message": exc.message, "code": exc.code}
    )
