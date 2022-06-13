"""GetCandidatesWithCounterOfVotesResponse Schema."""
from typing import Optional
from pydantic import BaseModel
from project.enums import Categories


class GetCandidatesWithCounterOfVotesResponse(BaseModel):
    id: int
    name: str
    description: str
    category: Categories
    picture: Optional[str]
    positive_votes: int
    positive_votes_pct: float
    negative_votes: int
    negative_votes_pct: float
    total_votes: int

    class Config:
        orm_mode = True
        allow_mutation = True
