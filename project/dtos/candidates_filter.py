"""CandidateFilter dto."""
from typing import List
from datetime import date
from starlette.datastructures import QueryParams
from project.utils.query_params_func import query_param_date, query_param_to_list_str


class CandidatesFilterDto:
    def __init__(self, from_date_created_at: date = None, categories: List[str] = None):
        self.from_date_created_at = from_date_created_at
        self.categories = categories

    @classmethod
    def from_query_params(cls, query_params: QueryParams):
        """Create dto class from query params"""
        from_date_created_at = query_param_date(query_param_value=query_params.get('from_date_created_at'))
        categories = query_param_to_list_str(query_param_value=query_params.get('categories'))

        return cls(from_date_created_at, categories)