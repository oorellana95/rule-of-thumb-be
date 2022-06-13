"""GetAllEmailsResponse Schema."""
from pydantic import BaseModel


class GetAllEmailsResponse(BaseModel):
    email: str

    class Config:
        orm_mode = True
        allow_mutation = True
