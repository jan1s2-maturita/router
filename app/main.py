from fastapi import FastAPI, Depends
# from middlewares import AuthMiddleware, LogMiddleware, ExceptionMiddleware
from .routers import forward

app = FastAPI()
# app = FastAPI()

# Define the internal routes for each microservice
# Apply the middleware to the FastAPI app
# app.middleware("http")(AuthMiddleware)
# app.middleware("http")(LogMiddleware)
# app.middleware("http")(ExceptionMiddleware)
app.include_router(forward.router)

