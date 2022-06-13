"""Candidates Router."""
from fastapi import APIRouter, Depends, status
from project import use_cases
from project.schemas.votes import UpgradeVoteRequest
from project.services import database
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/votes",
    tags=['Votes']
)

get_db = database.get_db


@router.put('/{candidate_id}', status_code=status.HTTP_202_ACCEPTED)
def upgrade_vote(candidate_id: int, request: UpgradeVoteRequest, db: Session = Depends(get_db)):
    """Create or update a new vote."""
    # TODO Get user_id from token.
    return use_cases.votes.upgrade_votes(db, user_id=request.user_id, candidate_id=candidate_id,
                                         veredict=request.veredict)
