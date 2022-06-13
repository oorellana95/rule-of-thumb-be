def test_given_no_data_it_should_return_valid_response(app_testing, sql_cleaner):
    response = app_testing.client.get('/candidates')

    assert response.status_code == 200
    assert response.json() == []


def test_given_data_it_should_return_valid_response(app_testing, sql_loader):
    sql_loader.load_file("integration/routers/_fixtures/candidates/test_list_candidates_with_votes.sql")
    response = app_testing.client.get('/candidates')

    assert response.status_code == 200
    assert response.json() == [
        {'id': 1, 'name': 'Kanye West', 'description': 'Born in Atlanta and raised in Chicago, West was first known as a producer for Roc-A-Fella Records in the early 2000s, producing singles for several mainstream artists.', 'category': 'entertainment', 'picture': None, 'positive_votes': 0, 'positive_votes_pct': 0.0, 'negative_votes': 3, 'negative_votes_pct': 1.0, 'total_votes': 3},
        {'id': 2, 'name': 'Mark Zuckerberg', 'description': 'Born in White Plains, New York, Zuckerberg attended Harvard University, where he launched the Facebook social networking service from his dormitory room on February 4, 2004.', 'category': 'business', 'picture': None, 'positive_votes': 1, 'positive_votes_pct': 0.333, 'negative_votes': 2, 'negative_votes_pct': 0.667, 'total_votes': 3},
        {'id': 3, 'name': 'Cristina Fernández de Kirchner', 'description': 'Her first term of office started with a conflict with the agricultural sector, and her proposed taxation system was rejected.', 'category': 'politics', 'picture': None, 'positive_votes': 0, 'positive_votes_pct': 0.0, 'negative_votes': 3, 'negative_votes_pct': 1.0, 'total_votes': 3},
        {'id': 4, 'name': 'Malala Yousafzai', 'description': 'The daughter of educational activist Ziauddin, Yousafzai was born to a Pashtun family in Mingora, Khyber Pakhtunkhwa, Pakistan. Her family came to run a chain of schools in the region.', 'category': 'politics', 'picture': None, 'positive_votes': 1, 'positive_votes_pct': 1.0, 'negative_votes': 0, 'negative_votes_pct': 0.0, 'total_votes': 1},
        {'id': 5, 'name': 'Elon Musk', 'description': 'In 2002, Musk founded SpaceX, an aerospace manufacturer and space transport services company, of which he is CEO, CTO, and lead designer.', 'category': 'business', 'picture': None, 'positive_votes': 0, 'positive_votes_pct': 0.0, 'negative_votes': 0, 'negative_votes_pct': 0.0, 'total_votes': 0},
        {'id': 6, 'name': 'Greta Thumberg', 'description': "Thunberg's activism started after convincing her parents to adopt several lifestyle choices to reduce their own carbon footprint.", 'category': 'environment', 'picture': None, 'positive_votes': 1, 'positive_votes_pct': 0.333, 'negative_votes': 2, 'negative_votes_pct': 0.667, 'total_votes': 3}]
