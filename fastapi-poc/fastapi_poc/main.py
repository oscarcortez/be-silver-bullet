from fastapi import FastAPI
from models.movie import Movie
from config.database import Session, engine, Base

app = FastAPI(
    title="aplicacion con fastapi",
    version="0.0.1"
)

Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}

