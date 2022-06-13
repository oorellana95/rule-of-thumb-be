from datetime import date, datetime
from typing import Optional, List
from project.exceptions.validation_exception import InputValidationException


def query_param_date(query_param_value: Optional[str], query_param_key="date") -> date:
    """Given a string query_param with format date, return the date object."""
    if query_param_value:
        try:
            return datetime.strptime(query_param_value, '%Y-%m-%d').date()
        except Exception:
            raise InputValidationException(f"Incorrect query param {query_param_key}. "
                                           f"It must be valid date with format %Y-%m-%d")


def query_param_to_list_str(query_param_value: Optional[str]) -> List[str]:
    """Given a query_param as string, return the list of strings of this query_param."""
    return None if query_param_value is None else query_param_value.split(',')

