def test_given_no_candidates_it_should_throw_an_exception(app_testing, sql_cleaner):
    response = app_testing.client.delete(
            '/candidates/15',
            headers={"X-Token": "coneofsilence"},
            json={}
        )

    assert response.status_code == 422
    assert response.json() == {
        'code': 'ERROR.RESPONSE',
        'message': 'Failed to execute method DELETE: http://testserver/candidates/15. Candidate with id 15 not found.'
    }


def test_given_candidate_it_should_remove_it_from_database(app_testing, sql_loader):
    sql_loader.load_file("integration/routers/_fixtures/candidates/test_delete_candidate.sql")
    response = app_testing.client.delete(
            '/candidates/2',
            headers={"X-Token": "coneofsilence"},
            json={}
        )

    assert response.status_code == 202
    assert response.json() == "Candidate with id 2 has successfully been deleted."