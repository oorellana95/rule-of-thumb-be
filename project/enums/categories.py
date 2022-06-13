"""Categories enum."""
from enum import Enum


# Note: Since it is for learning purposes, I created this enum to be used as a column in Candidate.
# In a real project, the creation of a new table should be considered instead of creating this enum.
class Categories(Enum):
    ENTERTAINMENT = 'entertainment'
    BUSINESS = 'business'
    POLITICS = 'politics'
    ENVIRONMENT = 'environment'
