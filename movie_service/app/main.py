from fastapi import FastAPI
from app.api.movies import movies

# Create the FastAPI instance
app = FastAPI()
app.include_router(movies)
