from fastapi import APIRouter, HTTPException, status

from fastapi_tutorial.qb_rating.models import QuarterBackStatistics
from fastapi_tutorial.qb_rating.service import calculate_quarterback_rating


router = APIRouter(prefix="/quarterback_rating")


@router.get("/")
async def get_passer_rating(stats: QuarterBackStatistics) -> float:
    if stats.attempts == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Quarterback attempts can not be zero.",
        )

    return round(calculate_quarterback_rating(stats), 1)
