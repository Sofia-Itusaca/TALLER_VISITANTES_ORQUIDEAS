from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.weather import router

app = FastAPI(
    title="Clima Visitantes - Las Orquídeas",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "service": "Clima Visitantes - Las Orquídeas",
        "status": "ok",
    }
