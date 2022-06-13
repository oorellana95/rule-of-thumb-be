"""Users Router."""
from typing import List
from fastapi import APIRouter, Depends, status
from project.schemas.users import GetAllEmailsResponse
from project.services import database
from sqlalchemy.orm import Session
from project import repositories

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

get_db = database.get_db


@router.get(path='/emails', response_model=List[GetAllEmailsResponse], status_code=status.HTTP_200_OK)
def get_all_emails_from_active_users(db: Session = Depends(get_db)):
    return repositories.users.get_all_emails_from_active_users(db)
