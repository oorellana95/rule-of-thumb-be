from project.use_cases.votes.upgrade_votes import veredict_to_tinyint


def test_given_a_veredict_none_it_should_return_none():
    veredict = None
    response = veredict_to_tinyint(veredict)
    assert response is None


def test_given_a_veredict_true_it_should_return_1():
    veredict = True
    response = veredict_to_tinyint(veredict)
    assert response == 1


def test_given_a_veredict_false_it_should_return_0():
    veredict = False
    response = veredict_to_tinyint(veredict)
    assert response == 0
