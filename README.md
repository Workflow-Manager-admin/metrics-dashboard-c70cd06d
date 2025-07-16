# metrics-dashboard-c70cd06d

## Kavia Backend - Metrics API

This project serves metrics and mock data for the frontend dashboard using FastAPI.

### How to run the backend locally

1. Install requirements:
    ```
    pip install -r kavia_backend/requirements.txt
    ```
2. Create a `.env` file in `kavia_backend/` to optionally configure:
    - `BACKEND_PORT` (default: 3001)
    - `BACKEND_HOST` (default: 0.0.0.0)
3. Run (from repository root):
    ```
    python -m kavia_backend.src.api.main
    ```
   or via `uvicorn` for hot reload:
    ```
    uvicorn kavia_backend.src.api.main:app --reload --port 3001
    ```

### API Endpoints

- `GET /metrics` – Returns a list of app generation metric records in JSON format (mocked, S3-ready for future).
- `GET /` – Health check.

### Notes

- All configuration is via environment variables (see `.env`).
- Mock metrics logic is structured to enable easy replacement with S3 file fetch.