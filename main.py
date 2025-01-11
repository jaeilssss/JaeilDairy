from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from src.controller.user_router import user_router
from src.common.exception.exception import BaseExceptionHanlder
from lifespan import life_span

print("main.py")
app = FastAPI(lifespan=life_span)
app.include_router(router=user_router, prefix="/user", tags=["유저 API"])


@app.exception_handler(BaseExceptionHanlder)
async def base_exception_handler(request: Request, exc: BaseExceptionHanlder):
    return JSONResponse(
        status_code=exc.status_code, content={"message": exc.message, "code": exc.code}
    )
