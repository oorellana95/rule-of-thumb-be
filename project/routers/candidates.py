"""Candidates Router."""
from typing import List
from fastapi import APIRouter, Depends, status, Request
from project import use_cases, repositories
from project.dtos import CandidatesFilterDto
from project.exceptions.response_exception import NotFoundException
from project.models import Candidate
from project.schemas.candidates import GetCandidatesWithCounterOfVotesResponse, UpgradeCandidateResponse, \
    UpgradeCandidateRequest
from project.services import database
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/candidates",
    tags=['Candidates']
)

get_db = database.get_db


@router.get(path='', response_model=List[GetCandidatesWithCounterOfVotesResponse],
            status_code=status.HTTP_200_OK)
def list_candidates_with_votes(request: Request, db: Session = Depends(get_db)):
    """Given query params returns a filtered list of candidates."""
    candidates_filter = CandidatesFilterDto.from_query_params(request.query_params)

    return use_cases.candidates.get_candidates_with_count_of_votes(db, candidates_filter)


@router.post('', response_model=UpgradeCandidateResponse, status_code=status.HTTP_201_CREATED)
def create_candidate(request: UpgradeCandidateRequest, db: Session = Depends(get_db)):
    """Create a new candidate."""
    candidate = Candidate(name=request.name,
                          description=request.description,
                          category=request.category,
                          picture=request.picture)

    return repositories.candidates.create(db, candidate=candidate)


@router.put('/{candidate_id}', response_model=UpgradeCandidateResponse, status_code=status.HTTP_202_ACCEPTED)
def update_candidate(candidate_id: int, request: UpgradeCandidateRequest, db: Session = Depends(get_db)):
    """Create a new candidate."""
    candidate = repositories.candidates.get_by_id(db, candidate_id=candidate_id)
    if candidate:
        candidate.name = request.name
        candidate.description = request.description
        candidate.category = request.category
        candidate.picture = request.picture
        repositories.candidates.update(db, candidate=candidate)
        return candidate
    else:
        raise NotFoundException(f"Candidate with id {candidate_id} not found.")


@router.delete('/{candidate_id}', status_code=status.HTTP_202_ACCEPTED)
def delete_candidate(candidate_id: int, db: Session = Depends(get_db)):
    """Delete a candidate."""
    candidate = repositories.candidates.get_by_id(db, candidate_id=candidate_id)
    if candidate:
        repositories.candidates.delete(db, candidate=candidate)
        return f"Candidate with id {candidate_id} has successfully been deleted."
    raise NotFoundException(f"Candidate with id {candidate_id} not found.")
