import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from src.api.metrics import router as metrics_router

load_dotenv()  # Load .env variables

app = FastAPI(
    title="Kavia Metrics Backend",
    description="Serves app generation metrics data for the metrics-dashboard application.",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(metrics_router)

@app.get("/", summary="Health Check", tags=["Health"])
def health_check():
    """
    Health check endpoint to verify API is up.
    Returns a plain status message.
    """
    return {"message": "Healthy"}


# Application server entrypoint for local/dev use
if __name__ == "__main__":
    import uvicorn

    # Read port from ENV (default 3001)
    port = int(os.environ.get("BACKEND_PORT", 3001))
    host = os.environ.get("BACKEND_HOST", "0.0.0.0")
    uvicorn.run("src.api.main:app", host=host, port=port, reload=True)
