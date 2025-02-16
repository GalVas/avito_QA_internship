from test_cases import current_item_body, current_item_id, positive_test_case_get_seller_id_items, \
    positive_test_case_seller_without_items, test_cases_seller_id_items, negative_test_cases_get_seller_items
from data import headers
from stand_request import get_new
import pytest
from jsonschema import validate, ValidationError

# Ручка {{baseUrl}}/api/1/:sellerID/item - Получить все объявления по идентификатору продавца


# Проверяем код состояния ответов для всех тест-кейсов для данного endpoint
@pytest.mark.parametrize('test_case', test_cases_seller_id_items,
                         ids=[tc.test_name for tc in test_cases_seller_id_items])
def test_response_status_code(test_case):
    response = get_new(headers.copy(), test_case.data)
    assert response.status_code == test_case.expected_status_code, f'Failed: {test_case.test_name}, ' \
                                                                   f'{test_case.description}'


# отдельная функция для проверок значений параметров - вывод всех параметров с ошибками
def assert_response_params(response, expected_item_id, expected_item_body):
    response_data = response.json()[len(response.json())-1]  # проверяем последнее добавленное объявление
    errors = []
    if response_data['id'] != expected_item_id:
        errors.append(f"ID не совпадают, ОР:{expected_item_id}, ФР:{response_data['id']}")
    if response_data['sellerId'] != expected_item_body['sellerID']:
        errors.append(f"sellerID не совпадают, ОР:{expected_item_body['sellerID']}, ФР:{response_data['sellerId']}")
    if response_data['name'] != expected_item_body['name']:
        errors.append(f"name не совпадают, ОР:{expected_item_body['name']}, ФР:{response_data['name']}")
    if response_data['price'] != expected_item_body['price']:
        errors.append(f"price не совпадают, ОР:{expected_item_body['price']}, ФР:{response_data['price']}")
    if response_data['statistics']['likes'] != expected_item_body['statistics']['likes']:
        errors.append(f"likes не совпадают, ОР:{expected_item_body['statistics']['likes']}, "
                      f"ФР:{response_data['statistics']['likes']}")
    if response_data['statistics']['viewCount'] != expected_item_body['statistics']['viewCount']:
        errors.append(f"viewCount не совпадают, ОР:{expected_item_body['statistics']['viewCount']}, "
                      f"ФР:{response_data['statistics']['viewCount']}")
    if response_data['statistics']['contacts'] != expected_item_body['statistics']['contacts']:
        errors.append(f"contacts не совпадают, ОР:{expected_item_body['statistics']['contacts']}, "
                      f"ФР:{response_data['statistics']['contacts']}")

    if errors:
        assert False, "Validation errors:\n" + "\n".join(errors)


# проверяем значения параметров объявления (позитивный сценарий)
@pytest.mark.parametrize('test_case', positive_test_case_get_seller_id_items,
                         ids=[tc.test_name for tc in positive_test_case_get_seller_id_items])
def test_positive_assert_response_params_seller_id_items(test_case):
    response = get_new(headers.copy(), test_case.data)
    assert_response_params(response, current_item_id, current_item_body)


# проверяем позитивный сценарий, когда у существующего продавца нет объявлений
@pytest.mark.parametrize('test_case', positive_test_case_seller_without_items,
                         ids=[tc.test_name for tc in positive_test_case_seller_without_items])
def test_positive_assert_response_params_seller_id_without_items(test_case):
    response = get_new(headers.copy(), test_case.data)
    assert response.json() == []


# Проверяем структуру ответа (негативные сценарии)
@pytest.mark.parametrize('test_case', negative_test_cases_get_seller_items,
                         ids=[tc.test_name for tc in negative_test_cases_get_seller_items])
def test_negative_assert_response_params_incorrect_seller_id(test_case):
    response = get_new(headers.copy(), test_case.data)
    try:
        validate(instance=response.json(), schema=test_case.expected_schema)
        assert True
    except ValidationError as e:
        assert False, f"Validation error: {e.message}"
