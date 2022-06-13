"""UpgradeVoteRequest Schema."""
from typing import Optional

from pydantic import BaseModel


class UpgradeVoteRequest(BaseModel):
    user_id: int
    veredict: Optional[bool]

    class Config:
        orm_mode = True
        allow_mutation = True
