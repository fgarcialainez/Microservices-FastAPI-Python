from fastapi import FastAPI
from app.api.movies import movies
from app.api.db import metadata, database, engine

# Create all tables stored in this metadata
metadata.create_all(engine)

# Create the FastAPI instance
app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(movies)
