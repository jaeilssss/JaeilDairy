from fastapi import FastAPI

app = FastAPI(
    lifespan= life_span,
)