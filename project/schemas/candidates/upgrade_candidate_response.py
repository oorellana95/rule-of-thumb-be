"""UpgradeCandidateResponse Schema. It is used for create and update candidates."""
from typing import Optional
from pydantic import BaseModel
from project import enums


class UpgradeCandidateResponse(BaseModel):
    id: str
    name: str
    description: str
    category: enums.Categories
    picture: Optional[str]

    class Config:
        orm_mode = True
        allow_mutation = True
