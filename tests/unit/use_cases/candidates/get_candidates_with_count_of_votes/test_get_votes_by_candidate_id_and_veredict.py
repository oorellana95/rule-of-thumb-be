from project.use_cases.candidates.get_candidates_with_count_of_votes import get_votes_by_candidate_id_and_veredict
from tests._tools.dict_to_obj import DictToObj


def test_given_no_votes_it_should_return_0():
    votes = []
    response = get_votes_by_candidate_id_and_veredict(votes=votes, candidate_id=1, veredict=None)
    assert response == 0


def test_given_votes_but_candidate_id_do_not_coincide_should_return_0():
    votes = [DictToObj({'candidate_id': 2, 'veredict': True})]
    response = get_votes_by_candidate_id_and_veredict(votes=votes, candidate_id=1, veredict=None)
    assert response == 0


def test_given_votes_and_valid_candidate_id_should_return_valid_response():
    votes = [DictToObj({'candidate_id': 2, 'veredict': True, 'units': 5}),
             DictToObj({'candidate_id': 2, 'veredict': False, 'units': 2})]
    response = get_votes_by_candidate_id_and_veredict(votes=votes, candidate_id=2, veredict=True)
    assert response == 5



