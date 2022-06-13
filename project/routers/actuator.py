"""Actuator Router."""
from fastapi import APIRouter, status

router = APIRouter(
    prefix="/actuator",
    tags=['Actuator']
)


@router.get(path='/health-check', status_code=status.HTTP_200_OK)
def health_check():
    """Health-check endpoint to verify that server is working."""
    return "OK"
