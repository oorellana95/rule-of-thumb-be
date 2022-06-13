"""Candidates Repository."""
from typing import Iterator
from sqlalchemy.orm import Session
from project.dtos import CandidatesFilterDto
from project.utils import sqlalchemy_filter_func
from project.models import Candidate


def add_candidates_filter(query, candidate_filter: CandidatesFilterDto):
    """Given a query and the candidates filters, adds the candidates statements to the query."""
    query = sqlalchemy_filter_func.higher_or_equal(query,
                                                   value_from_entity=Candidate.created_at,
                                                   value_from_filter=candidate_filter.from_date_created_at)
    query = sqlalchemy_filter_func.in_(query,
                                       value_from_entity=Candidate.category,
                                       values_from_filter=candidate_filter.categories)
    return query


def get_by_id(db: Session, candidate_id: int) -> Candidate:
    """Given an id, return the candidate from database."""
    return db.query(Candidate).get(candidate_id)


def get_by_filter(db: Session, candidate_filter: CandidatesFilterDto) \
        -> Iterator:
    """Return candidates from the table candidates."""
    query = db.query(
        Candidate.id,
        Candidate.name,
        Candidate.description,
        Candidate.category,
        Candidate.picture)

    query = add_candidates_filter(query, candidate_filter)
    return query.all()


def create(db: Session, candidate: Candidate):
    """Given a candidate, creates it in the database."""
    db.add(candidate)
    db.commit()
    db.refresh(candidate)
    return candidate


def update(db: Session, candidate: Candidate):
    """Given a candidate, updates it in the database."""
    db.merge(candidate)
    db.commit()
    db.refresh(candidate)
    return candidate


def delete(db: Session, candidate: Candidate):
    """Given a candidate, remove the candidate from database."""
    db.delete(candidate)
    db.commit()

