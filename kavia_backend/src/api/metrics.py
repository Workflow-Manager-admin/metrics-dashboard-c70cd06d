from typing import List, Optional
from datetime import datetime
from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field

# PUBLIC_INTERFACE
class MetricRecord(BaseModel):
    """Represents a single app generation metric record."""
    app_name: str = Field(..., description="Name of the generated application")
    model: str = Field(..., description="Model used for generation")
    cga_version: str = Field(..., description="Code Generation Agent version")
    creation_time: datetime = Field(..., description="UTC ISO8601 timestamp of generation")
    cost: float = Field(..., description="Monetary cost of generation in USD")
    project_link: Optional[str] = Field(None, description="URL linking to the generated project")
    tokens_used: Optional[int] = Field(None, description="Number of tokens used")
    duration_seconds: Optional[float] = Field(None, description="Generation duration in seconds")

# In-memory mock data (future: fetched from S3 or other backend)
MOCK_METRICS: List[MetricRecord] = [
    MetricRecord(
        app_name="Sales Dashboard",
        model="gpt-4-turbo-builder",
        cga_version="1.2.3",
        creation_time=datetime(2024, 6, 20, 15, 30),
        cost=2.75,
        project_link="https://example.com/projects/sales-dashboard",
        tokens_used=15438,
        duration_seconds=27.8,
    ),
    MetricRecord(
        app_name="Inventory Tracker",
        model="gpt-3.5-data-final",
        cga_version="1.2.3",
        creation_time=datetime(2024, 6, 18, 12, 44),
        cost=1.50,
        project_link="https://example.com/projects/inventory-tracker",
        tokens_used=10423,
        duration_seconds=18.2,
    ),
    MetricRecord(
        app_name="Customer Portal",
        model="gpt-4-turbo-builder",
        cga_version="1.2.2",
        creation_time=datetime(2024, 6, 14, 8, 17),
        cost=3.20,
        project_link="https://example.com/projects/customer-portal",
        tokens_used=19999,
        duration_seconds=33.1,
    ),
]

router = APIRouter(
    tags=["Metrics"],
)

# Dependency for future expansion
def get_metrics_source():
    """
    Resolve metrics data source.
    Future: fetch from S3 or other store using environment/config.
    """
    return MOCK_METRICS

# PUBLIC_INTERFACE
@router.get(
    "/metrics",
    response_model=List[MetricRecord],
    summary="Get Mock App Generation Metrics",
    description="Returns a list of app generation metric records (currently mocked in-memory, future-proofed for S3 or other backend integration).",
    tags=["Metrics"],
)
async def get_metrics(data=Depends(get_metrics_source)):
    """
    Retrieve a list of app generation metric records.

    Returns:
        List[MetricRecord]: A list of metric records (mocked data currently).
    """
    return data
