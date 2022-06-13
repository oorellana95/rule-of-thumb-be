def test_given_no_data_it_should_return_valid_response(app_testing, sql_cleaner):
    response = app_testing.client.get('/users/emails')

    assert response.status_code == 200
    assert response.json() == []


def test_given_data_it_should_return_valid_response(app_testing, sql_loader):
    sql_loader.load_file("integration/routers/_fixtures/users/test_get_all_emails_from_active_users.sql")
    response = app_testing.client.get('/users/emails')

    assert response.status_code == 200
    assert response.json() == [
        {'email': 'oscar@gmail.com'},
        {'email': 'raquel@gmail.com'},
        {'email': 'viviana@gmail.com'},
        {'email': 'lizeth@gmail.com'}
    ]
