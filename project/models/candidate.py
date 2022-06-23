"""Candidate data model definition."""
from sqlalchemy import Column, String, Integer, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from project import enums
from project.services.database import Base


class Candidate(Base):
    """Candidate table definition."""
    __tablename__ = 'candidates'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=False)
    category = Column(Enum(enums.Categories), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False,
                        server_default=func.now())
    last_updated = Column(DateTime(timezone=True), nullable=False,
                          server_default=func.now(), onupdate=func.now())

    # Foreign key objects
    votes = relationship('Vote', lazy='joined', cascade='all, delete')
