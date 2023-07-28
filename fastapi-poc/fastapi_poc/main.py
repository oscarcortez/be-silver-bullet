from fastapi import FastAPI
#from models.movie import Movie
#from config.database import Session, engine, Base
from newdirectory.archivo import algo

app = FastAPI(
    title="aplicacion con fastapi",
    version="0.0.1"
)

#Base.metadata.create_all(bind=engine)

xx = algo()

@app.get("/")
async def root():
    return {"message": f'Hello World{xx.printer()}'}

