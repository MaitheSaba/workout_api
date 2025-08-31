from fastapi import FastAPI
from routers import api_router
from fastapi_pagination import add_pagination

app = FastAPI(title='WorkoutApi')
add_pagination(app)
app.include_router(api_router)
