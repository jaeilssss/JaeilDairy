from fastapi import FastAPI
from src.controller.user_router import user_router
from lifespan import life_span
app = FastAPI(
   lifespan= life_span
)
app.include_router(router=user_router, prefix="/user", tags= ["유저 API"])
