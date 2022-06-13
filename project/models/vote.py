"""Vote data model definition."""
from sqlalchemy import Column, Integer, DateTime, Boolean, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import JSON
from project.services.database import Base


class Vote(Base):
    """Votes table definition."""
    __tablename__ = 'votes'
    user_id = Column(Integer, ForeignKey('users.id'))
    candidate_id = Column(Integer, ForeignKey('candidates.id'))
    veredict = Column(Boolean, nullable=True)
    historical_veredicts = Column(JSON)
    updated_at = Column(DateTime(timezone=True), nullable=False,
                        server_default=func.now(), onupdate=func.now())

    __table_args__ = (
        PrimaryKeyConstraint(user_id, candidate_id),
        {},
    )
