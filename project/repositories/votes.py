"""Votes Repository."""
from sqlalchemy import func
from sqlalchemy.orm import Session
from project.dtos import VotesFilterDto
from project.models.vote import Vote
from project.utils import sqlalchemy_filter_func


def add_votes_filter(query, votes_filter: VotesFilterDto):
    """Given a query and the votes filters, adds the votes statements to the query."""
    query = sqlalchemy_filter_func.equal(query, value_from_entity=Vote.user_id, value_from_filter=votes_filter.user_id)
    query = sqlalchemy_filter_func.in_(query, value_from_entity=Vote.candidate_id, values_from_filter=votes_filter.candidate_ids)
    query = sqlalchemy_filter_func.in_(query, value_from_entity=Vote.veredict, values_from_filter=votes_filter.veredict_types)
    return query


def get_votes_grouped_by_candidate_id_and_veredict(db: Session, votes_filter: VotesFilterDto):
    """Return candidates from the table candidates."""
    query = db.query(Vote.candidate_id, Vote.veredict, func.count().label('units'))
    query = add_votes_filter(query, votes_filter)
    query = query.group_by(Vote.candidate_id, Vote.veredict)

    return query.all()


def get_vote_by_user_id_and_candidate_id(db: Session, user_id: int, candidate_id: int):
    return db.query(Vote).get((user_id, candidate_id))


def create(db: Session, vote: Vote):
    """Given a vote, creates it in the database."""
    db.add(vote)
    db.commit()
    db.refresh(vote)
    return vote


def update(db: Session, vote: Vote):
    """Given a vote, updates it in the database."""
    db.merge(vote)
    db.commit()
    db.refresh(vote)
    return vote
