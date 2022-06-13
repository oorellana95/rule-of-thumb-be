"""VotesFilter dto."""
from typing import List


class VotesFilterDto:
    def __init__(self, user_id: int = None, candidate_ids: List[int] = None, veredict_types: List[bool] = None):
        self.user_id = user_id
        self.candidate_ids = candidate_ids
        self.veredict_types = veredict_types
