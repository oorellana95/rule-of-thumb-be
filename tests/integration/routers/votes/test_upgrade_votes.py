import pytest


def test_given_no_data_it_should_throw_an_exception(app_testing, sql_cleaner):
    with pytest.raises(Exception) as exc_info:
        app_testing.client.put(
            '/votes/15',
            headers={"X-Token": "coneofsilence"},
            json={'user_id': 1,
                  'veredict': True}
        )

    assert exc_info.typename == 'IntegrityError'


def test_given_a_vote_it_should_update_fields_and_return_valid_response(app_testing, sql_loader_cl):
    sql_loader_cl.load_file("integration/routers/_fixtures/votes/test_upgrade_vote.sql")
    response = app_testing.client.put(
        '/votes/1',
        headers={"X-Token": "coneofsilence"},
        json={'user_id': 2,
              'veredict': True}
    )

    assert response.status_code == 202
    assert response.json() == 'Your vote has successfully been updated.'


def test_given_a_vote_it_should_create_it_and_return_valid_response(app_testing, sql_loader_cl):
    sql_loader_cl.load_file("integration/routers/_fixtures/votes/test_upgrade_vote.sql")
    response = app_testing.client.put(
        '/votes/2',
        headers={"X-Token": "coneofsilence"},
        json={'user_id': 2,
              'veredict': True}
    )

    assert response.status_code == 202
    assert response.json() == 'Your vote has successfully been registered.'
