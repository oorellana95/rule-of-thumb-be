"""User data model definition."""
from sqlalchemy import Column, String, Integer, DateTime, Text, Boolean
from sqlalchemy.sql import func
from project.services.database import Base


# Note: Password field is nullable since it is expected you can log in using credentials from providers.
class User(Base):
    """Users table definition."""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True, nullable=False)
    name = Column(String(50), nullable=False)
    family_name = Column(String(50), nullable=True)
    password = Column(Text, nullable=True)
    enabled = Column(Boolean, nullable=False, default=1)
    created_at = Column(DateTime(timezone=True), nullable=False,
                        server_default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=False,
                        server_default=func.now(), onupdate=func.now())
