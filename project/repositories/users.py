"""Candidates Repository."""
from typing import Iterator
from sqlalchemy.orm import Session
from project.models import User
from project.utils import sqlalchemy_filter_func


def get_all_emails_from_active_users(db: Session) -> Iterator:
    """Return candidates from the table candidates."""
    query = db.query(User.email)
    query = sqlalchemy_filter_func.equal(query, value_from_entity=User.enabled, value_from_filter=True)
    return query.all()
