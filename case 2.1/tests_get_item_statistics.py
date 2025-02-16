from test_cases import current_item_body, test_cases_statistics_item_id, \
    positive_test_case_get_item_statistics, positive_test_case_item_created_without_statistics, \
    negative_test_cases_get_item_statistics_incorrect_id
from data import headers
from stand_request import get_new
import pytest
from jsonschema import validate, ValidationError

# Ручка {{baseUrl}}/api/1/statistic/:id - Получить статистику по айтем id


# Проверяем код состояния ответов для всех тест-кейсов для данного endpoint
@pytest.mark.parametrize('test_case', test_cases_statistics_item_id,
                         ids=[tc.test_name for tc in test_cases_statistics_item_id])
def test_response_status_code(test_case):
    response = get_new(headers.copy(), test_case.data)
    print(response.json())
    assert response.status_code == test_case.expected_status_code, f'Failed: {test_case.test_name}, ' \
                                                                   f'{test_case.description}'


# отдельная функция для проверок значений параметров - вывод всех параметров с ошибками
def assert_response_params(response, expected_item_body):
    response_data = response.json()[0]
    errors = []
    if response_data['likes'] != expected_item_body['statistics']['likes']:
        errors.append(f"likes не совпадают, ОР:{expected_item_body['statistics']['likes']}, "
                      f"ФР:{response_data['likes']}")
    if response_data['viewCount'] != expected_item_body['statistics']['viewCount']:
        errors.append(f"viewCount не совпадают, ОР:{expected_item_body['statistics']['viewCount']}, "
                      f"ФР:{response_data['viewCount']}")
    if response_data['contacts'] != expected_item_body['statistics']['contacts']:
        errors.append(f"contacts не совпадают, ОР:{expected_item_body['statistics']['contacts']}, "
                      f"ФР:{response_data['contacts']}")

    if errors:
        assert False, "Validation errors:\n" + "\n".join(errors)


# проверяем значения параметров (позитивный сценарий)
@pytest.mark.parametrize('test_case', positive_test_case_get_item_statistics,
                         ids=[tc.test_name for tc in positive_test_case_get_item_statistics])
def test_positive_assert_item_stat_response_params(test_case):
    response = get_new(headers.copy(), test_case.data)
    assert_response_params(response, current_item_body)


# отдельная функция для проверок значений параметров - вывод всех параметров с ошибками
def assert_response_params_are_0(response):
    response_data = response.json()[0]
    errors = []
    if response_data['likes'] != 0:
        errors.append(f"likes не совпадают, ОР:{0}, "f"ФР:{response_data['likes']}")
    if response_data['viewCount'] != 0:
        errors.append(f"viewCount не совпадают, ОР:{0}, "f"ФР:{response_data['viewCount']}")
    if response_data['contacts'] != 0:
        errors.append(f"contacts не совпадают, ОР:{0}, "f"ФР:{response_data['contacts']}")

    if errors:
        assert False, "Validation errors:\n" + "\n".join(errors)


# проверяем значения параметров - позитивный сценарий, когда объявление было создано без параметра statistics
@pytest.mark.parametrize('test_case', positive_test_case_item_created_without_statistics,
                         ids=[tc.test_name for tc in positive_test_case_item_created_without_statistics])
def test_item_created_without_statistics_params(test_case):
    response = get_new(headers.copy(), test_case.data)
    assert_response_params_are_0(response)


# Проверяем структуру ответа (негативные сценарии)
@pytest.mark.parametrize('test_case', negative_test_cases_get_item_statistics_incorrect_id,
                         ids=[tc.test_name for tc in negative_test_cases_get_item_statistics_incorrect_id])
def test_negative_assert_incorrect_id_item_response_schema(test_case):
    response = get_new(headers.copy(), test_case.data)
    try:
        validate(instance=response.json(), schema=test_case.expected_schema)
        assert True
    except ValidationError as e:
        assert False, f"Validation error: {e.message}"
