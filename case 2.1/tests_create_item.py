from data import headers
from configuration import CREATE_ITEM_PATH
from stand_request import post_new
from test_cases import create_item_all_test_cases
import pytest
from jsonschema import validate, ValidationError

# Ручка POST /api/1/item - создание объявления


# Проверяем код состояния ответов для всех тест-кейсов для данного endpoint
@pytest.mark.parametrize('test_case', create_item_all_test_cases,
                         ids=[tc.test_name for tc in create_item_all_test_cases])
def test_response_status_code(test_case):
    response = post_new(test_case.data, headers.copy(), CREATE_ITEM_PATH)
    assert response.status_code == test_case.expected_status_code, f'{test_case.test_name}, {test_case.description}'


# Проверяем структуру ответа (все тест-кейсы для данного endpoint)
@pytest.mark.parametrize('test_case', create_item_all_test_cases,
                         ids=[tc.test_name for tc in create_item_all_test_cases])
def test_response_schema(test_case):
    response = post_new(test_case.data, headers.copy(), CREATE_ITEM_PATH)
    try:
        validate(instance=response.json(), schema=test_case.expected_schema)
        assert True
    except ValidationError as e:
        assert False, f"Validation error: {e.message}"
