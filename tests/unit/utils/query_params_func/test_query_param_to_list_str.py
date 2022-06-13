from project.utils.query_params_func import query_param_to_list_str


def test_given_a_valid_year_it_should_return_the_number():
    string = "barcelona,medellin,miami"
    response = query_param_to_list_str(string)
    assert response == ['barcelona', 'medellin', 'miami']

