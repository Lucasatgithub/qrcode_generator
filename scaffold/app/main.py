from fastapi import FastAPI

from .database import Base, engine
from .routes import router

from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(title="QR Code Generator Prototype")
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # For development only
    allow_methods=["*"],
    allow_headers=["*"],
)
