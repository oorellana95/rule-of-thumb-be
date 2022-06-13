from datetime import date
import pytest
from project.exceptions.validation_exception import InputValidationException
from project.utils.query_params_func import query_param_date


def test_given_a_valid_date_it_should_return_the_date():
    input_date = "2022-02-25"
    response = query_param_date(input_date)
    assert response == date(2022, 2, 25)


def test_given_an_invalid_format_date_it_should_throw_exception():
    with pytest.raises(InputValidationException) as exc_info:
        input_date = "2022/02-25"
        query_param_date(input_date)

    assert exc_info.value.code == 'ERROR.VALIDATION'
    assert exc_info.value.message == 'Incorrect query param date. It must be valid date with format %Y-%m-%d'


def test_given_an_invalid_date_it_should_throw_exception():
    with pytest.raises(InputValidationException) as exc_info:
        input_date = "2022-02-30"
        query_param_date(input_date)

    assert exc_info.value.code == 'ERROR.VALIDATION'
    assert exc_info.value.message == 'Incorrect query param date. It must be valid date with format %Y-%m-%d'
