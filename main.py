from fastapi import FastAPI

from api.routes import router as api_router


app = FastAPI(title="AI Engine")


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(api_router, prefix="/api")

