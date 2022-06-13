def test_given_no_candidates_it_should_throw_an_exception(app_testing, sql_cleaner):
    response = app_testing.client.put(
        '/candidates/15',
        headers={"X-Token": "coneofsilence"},
        json={'name': 'Warren Buffet',
              'description': 'Warren Edward Buffett is an American business magnate, investor, and philanthropist. He is currently the chairman and CEO of Berkshire Hathaway.',
              'category': 'business'}
    )

    assert response.status_code == 422
    assert response.json() == {
        'code': 'ERROR.RESPONSE',
        'message': 'Failed to execute method PUT: http://testserver/candidates/15. Candidate with id 15 not found.'
    }


def test_given_candidate_it_should_update_fields_and_return_valid_response(app_testing, sql_loader_cl):
    sql_loader_cl.load_file("integration/routers/_fixtures/candidates/test_update_candidates.sql")
    response = app_testing.client.put(
        '/candidates/1',
        headers={"X-Token": "coneofsilence"},
        json={'name': 'Warren Buffet',
              'description': 'Warren Edward Buffett is an American business magnate, investor, and philanthropist. He is currently the chairman and CEO of Berkshire Hathaway.',
              'category': 'business'}
    )

    assert response.status_code == 202
    assert response.json() == {
        'id': '1',
        'name': 'Warren Buffet',
        'description': 'Warren Edward Buffett is an American business magnate, investor, and philanthropist. He is currently the chairman and CEO of Berkshire Hathaway.',
        'category': 'business',
        'picture': None
    }