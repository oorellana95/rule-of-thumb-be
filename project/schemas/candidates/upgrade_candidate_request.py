"""UpgradeCandidateRequest Schema."""
from typing import Optional
from pydantic import BaseModel
from project import enums


class UpgradeCandidateRequest(BaseModel):
    name: str
    description: str
    category: enums.Categories

    class Config:
        orm_mode = True
        allow_mutation = True
