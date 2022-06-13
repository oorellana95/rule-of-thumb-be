from datetime import date
from project.dtos import CandidatesFilterDto
from project.models import Candidate
from project.repositories.candidates import add_candidates_filter
from tests._tools.database.db_query_test import DbQueryTest, literal_query

db = DbQueryTest()


def test_given_no_data_in_candidates_filter_it_should_work_as_expected():
    candidates_filter = CandidatesFilterDto()
    query = db.session.query(Candidate.id)
    query = add_candidates_filter(query, candidates_filter)
    response = literal_query(query)

    assert response == 'SELECT candidates.id \nFROM candidates'


def test_given_candidates_filter_it_should_work_as_expected():
    candidates_filter = CandidatesFilterDto(from_date_created_at=date(2020, 1, 1),
                                            categories=['POLITICS', 'ENVIRONMENT'])

    query = db.session.query(Candidate.id)
    query = add_candidates_filter(query, candidates_filter)
    response = literal_query(query)

    assert response == "SELECT candidates.id \n" \
                       "FROM candidates \n" \
                       "WHERE candidates.created_at >= '2020-01-01' " \
                       "AND candidates.category IN ('POLITICS', 'ENVIRONMENT')"
