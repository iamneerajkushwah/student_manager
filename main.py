from fastapi import FastAPI
from routes.student import router

app = FastAPI()

app.include_router(router)