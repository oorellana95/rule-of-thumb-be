def test_given_candidates_it_should_create_and_persist_it_in_database(app_testing, sql_cleaner):
    response = app_testing.client.post(
        '/candidates',
        headers={"X-Token": "coneofsilence"},
        json={'name': 'Warren Buffet',
              'description': 'Warren Edward Buffett is an American business magnate, investor, and philanthropist. He is currently the chairman and CEO of Berkshire Hathaway.',
              'category': 'business'}
    )

    assert response.status_code == 201
    assert response.json() == {
        'id': '1',
        'name': 'Warren Buffet',
        'description': 'Warren Edward Buffett is an American business magnate, investor, and philanthropist. He is currently the chairman and CEO of Berkshire Hathaway.',
        'category': 'business',
        'picture': None
    }
