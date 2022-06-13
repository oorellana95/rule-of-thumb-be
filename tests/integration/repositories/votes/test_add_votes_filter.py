from project.dtos import VotesFilterDto
from project.models.vote import Vote
from project.repositories.votes import add_votes_filter
from tests._tools.database.db_query_test import DbQueryTest, literal_query

db = DbQueryTest()


def test_given_no_data_in_candidates_filter_it_should_work_as_expected():
    votes_filter = VotesFilterDto()
    query = db.session.query(Vote.user_id, Vote.candidate_id)
    query = add_votes_filter(query, votes_filter)
    response = literal_query(query)

    assert response == 'SELECT votes.user_id, votes.candidate_id \nFROM votes'


def test_given_candidates_filter_it_should_work_as_expected():
    votes_filter = VotesFilterDto(user_id=1, candidate_ids=[1, 2, 3], veredict_types=[True, False])

    query = db.session.query(Vote.user_id, Vote.candidate_id)
    query = add_votes_filter(query, votes_filter)
    response = literal_query(query)

    assert response == "SELECT votes.user_id, votes.candidate_id \n" \
                       "FROM votes \n" \
                       "WHERE votes.user_id = 1 " \
                       "AND votes.candidate_id IN (1, 2, 3) " \
                       "AND votes.veredict IN (true, false)"

