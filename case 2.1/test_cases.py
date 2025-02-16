from data import item_body, correct_data_response, incorrect_data_response
from utils import change_item_body, get_copy_of, get_item_id, create_url, create_seller_items_url
from configuration import GET_ITEM_PATH, GET_ITEM_STATISTICS_PATH, GET_SELLER_ID_ITEMS

# В данном файле описаны все тест-кейсы необходимые для проведения тестирования endpoints


class TestCase:
    def __init__(self, test_name, description, data, expected_status_code, expected_schema):
        self.test_name = test_name
        self.description = description
        self.data = data
        self.expected_status_code = expected_status_code
        self.expected_schema = expected_schema

# Ручка POST /api/1/item - создание объявления


# Позитивные сценарии для функционала создания объявления
positive_test_cases = [
    TestCase(test_name='CREATE_ITEM_001',
             description='Все поля заполнены корректно',
             data=item_body.copy(),
             expected_status_code=200,
             expected_schema=correct_data_response),

    TestCase(test_name='CREATE_ITEM_002',
             description='Переданы корректные данные - отсутствует необязательное поле statistics',
             data={key: value for key, value in item_body.items() if key != 'statistics'},
             expected_status_code=200,
             expected_schema=correct_data_response)
]

# Позитивные сценарии для функционала создания объявления, когда параметры statistics равны 0
positive_test_cases_zero_statistics_param = [
    TestCase(test_name='CREATE_ITEM_003',
             description='Переданы корректные данные - параметр contacts = 0',
             data=change_item_body('contacts', 0),
             expected_status_code=200,
             expected_schema=correct_data_response),

    TestCase(test_name='CREATE_ITEM_004',
             description='Переданы корректные данные - параметр likes = 0',
             data=change_item_body('likes', 0),
             expected_status_code=200,
             expected_schema=correct_data_response),

    TestCase(test_name='CREATE_ITEM_005',
             description='Переданы корректные данные - параметр viewCount = 0',
             data=change_item_body('viewCount', 0),
             expected_status_code=200,
             expected_schema=correct_data_response)
]

# Негативные сценарии - нет обязательных параметров тела запроса
negative_test_cases_no_required_param = [
    TestCase(test_name='NEG_CREATE_ITEM_001',
             description='Отсутствует обязательный параметр sellerID',
             data={key: value for key, value in item_body.items() if key != 'sellerID'},  # словарь без sellerID
             expected_status_code=400,
             expected_schema=incorrect_data_response),

    TestCase(test_name='NEG_CREATE_ITEM_002',
             description='Отсутствует обязательный параметр name',
             data={key: value for key, value in item_body.items() if key != 'name'},
             expected_status_code=400,
             expected_schema=incorrect_data_response),

    TestCase(test_name='NEG_CREATE_ITEM_003',
             description='Отсутствует обязательный параметр price',
             data={key: value for key, value in item_body.items() if key != 'price'},
             expected_status_code=400,
             expected_schema=incorrect_data_response)
]

# Негативные сценарии - параметр sellerID
negative_test_cases_seller_id = [
    TestCase(test_name='NEG_CREATE_ITEM_004',
             description='Недопустимый тип данных для поля sellerID: str',
             data=change_item_body('sellerID', '1234345989'),
             expected_status_code=400,
             expected_schema=incorrect_data_response),

    TestCase(test_name='NEG_CREATE_ITEM_005',
             description='Большое значение int для поля sellerID',
             data=change_item_body('sellerID', 4*10**14),
             expected_status_code=400,
             expected_schema=incorrect_data_response),

    TestCase(test_name='NEG_CREATE_ITEM_006',
             description='Логически некорректное значение для поля sellerID: 0',
             data=change_item_body('sellerID', 0),
             expected_status_code=400,
             expected_schema=incorrect_data_response),

    TestCase(test_name='NEG_CREATE_ITEM_007',
             description='Логически некорректное значение для поля sellerID: -1',
             data=change_item_body('sellerID', -1),
             expected_status_code=400,
             expected_schema=incorrect_data_response)
]

# Негативные сценарии - параметр name
negative_test_cases_name = [
    TestCase(test_name='NEG_CREATE_ITEM_008',
             description='Недопустимый тип данных для поля name: int',
             data=change_item_body('name', 1111111111),
             expected_status_code=400,
             expected_schema=incorrect_data_response),

    TestCase(test_name='NEG_CREATE_ITEM_009',
             description='Пустое значение для поля name',
             data=change_item_body('name', ''),
             expected_status_code=400,
             expected_schema=incorrect_data_response)
]

# Негативные сценарии - параметр price
negative_test_cases_price = [
    TestCase(test_name='NEG_CREATE_ITEM_010',
             description='Недопустимый тип данных для поля price: str',
             data=change_item_body('price', '12345'),
             expected_status_code=400,
             expected_schema=incorrect_data_response),

    TestCase(test_name='NEG_CREATE_ITEM_011',
             description='Большое значение int для поля price',
             data=change_item_body('price', 4*10**14),
             expected_status_code=400,
             expected_schema=incorrect_data_response),

    TestCase(test_name='NEG_CREATE_ITEM_012',
             description='Логически некорректное значение для поля price: 0',
             data=change_item_body('price', 0),
             expected_status_code=400,
             expected_schema=incorrect_data_response),

    TestCase(test_name='NEG_CREATE_ITEM_013',
             description='Логически некорректное значение для поля price: -1',
             data=change_item_body('price', -1),
             expected_status_code=400,
             expected_schema=incorrect_data_response)
]

# Негативные сценарии - параметр statistics
negative_test_cases_statistics = [
    TestCase(test_name='NEG_CREATE_ITEM_014',
             description='Недопустимый тип данных для поля statistics: list',
             data=list({"sellerID": 1234345989, "name": "example", "price": 10,
                        "statistics": {"contacts": 5, "likes": 2, "viewCount": 8}}),
             expected_status_code=400,
             expected_schema=incorrect_data_response),

    TestCase(test_name='NEG_CREATE_ITEM_015',
             description='Пустое значение для поля statistics: {}',
             data={"sellerID": 1234345989, "name": "example", "price": 10, "statistics": {}},
             expected_status_code=400,
             expected_schema=incorrect_data_response)
]

# Негативные сценарии - параметр contacts
negative_test_cases_statistics_contacts = [
    TestCase(test_name='NEG_CREATE_ITEM_016',
             description='Недопустимый тип данных для поля contacts: str',
             data=change_item_body('contacts', '12345'),
             expected_status_code=400,
             expected_schema=incorrect_data_response),

    TestCase(test_name='NEG_CREATE_ITEM_017',
             description='Большое значение int для поля contacts',
             data=change_item_body('contacts', 4*10**14),
             expected_status_code=400,
             expected_schema=incorrect_data_response),

    TestCase(test_name='NEG_CREATE_ITEM_018',
             description='Логически некорректное значение для поля contacts: -1',
             data=change_item_body('contacts', -1),
             expected_status_code=400,
             expected_schema=incorrect_data_response)
]

# Негативные сценарии - параметр likes
negative_test_cases_statistics_likes = [
    TestCase(test_name='NEG_CREATE_ITEM_019',
             description='Недопустимый тип данных для поля likes: str',
             data=change_item_body('likes', '123'),
             expected_status_code=400,
             expected_schema=incorrect_data_response),

    TestCase(test_name='NEG_CREATE_ITEM_020',
             description='Большое значение int для поля likes',
             data=change_item_body('likes', 4*10**14),
             expected_status_code=400,
             expected_schema=incorrect_data_response),

    TestCase(test_name='NEG_CREATE_ITEM_021',
             description='Логически некорректное значение для поля likes: -1',
             data=change_item_body('likes', -1),
             expected_status_code=400,
             expected_schema=incorrect_data_response)
]

# Негативные сценарии - параметр viewCount
negative_test_cases_statistics_viewCount = [
    TestCase(test_name='NEG_CREATE_ITEM_022',
             description='Недопустимый тип данных для поля contacts: str',
             data=change_item_body('viewCount', '123'),
             expected_status_code=400,
             expected_schema=incorrect_data_response),

    TestCase(test_name='NEG_CREATE_ITEM_023',
             description='Большое значение int для поля viewCount',
             data=change_item_body('viewCount',  4*10**14),
             expected_status_code=400,
             expected_schema=incorrect_data_response),

    TestCase(test_name='NEG_CREATE_ITEM_024',
             description='Логически некорректное значение для поля viewCount: -1',
             data=change_item_body('viewCount',  -1),
             expected_status_code=400,
             expected_schema=incorrect_data_response)
]

# Собираем в один набор тест-кейсов для проверки параметров expected_status_code и expected_schema
create_item_all_test_cases = positive_test_cases + positive_test_cases_zero_statistics_param + \
            negative_test_cases_no_required_param + negative_test_cases_seller_id + negative_test_cases_name + \
            negative_test_cases_price + negative_test_cases_statistics + negative_test_cases_statistics_contacts + \
            negative_test_cases_statistics_likes + negative_test_cases_statistics_viewCount


# Проверки ручек GET

# переменная, которая хранит тело запроса без необязательного параметра statistics
item_body_without_statistics = {k: v for k, v in item_body.items() if k != 'statistics'}  # словарь без statistics
item_without_statistics_id = get_item_id(item_body_without_statistics)

# переменная, которая хранит тело запроса с параметром statistics
current_item_body = get_copy_of(item_body)
current_item_id = get_item_id(current_item_body)

# Ручка {{baseUrl}}/api/1/item/:id - Получение инфы об объявлении

# Позитивный сценарий - передаем корректный id существующего объявления
positive_test_case_get_item_info = [
    TestCase(test_name='GET_ITEM_INFO_001',
             description='Переданы корректные данные - id существующего объявления',
             data=create_url(GET_ITEM_PATH, current_item_id),
             expected_status_code=200,
             expected_schema=[])
]

# Негативные сценарии - параметр id
negative_test_cases_get_item_info_incorrect_id = [
    TestCase(test_name='NEG_GET_ITEM_INFO_001',
             description='Переданы некорректные данные - id несуществующего объявления',
             data=create_url(GET_ITEM_PATH, 'ffffffff-ffff-ffff-ffff-ffffffffffff'),
             expected_status_code=404,
             expected_schema=incorrect_data_response),

    TestCase(test_name='NEG_GET_ITEM_INFO_002',
             description='Переданы некорректные данные - пробел в качестве id объявления',
             data=create_url(GET_ITEM_PATH, ' '),
             expected_status_code=400,
             expected_schema=incorrect_data_response),

    TestCase(test_name='NEG_GET_ITEM_INFO_003',
             description='Переданы некорректные данные - отсутствуют "-" в id объявления',
             data=create_url(GET_ITEM_PATH, get_copy_of(current_item_id).replace('-', '')),
             expected_status_code=400,
             expected_schema=incorrect_data_response)
]

# Собираем в один набор тест-кейсов для проверки параметра expected_status_code
test_cases_info_item_id = positive_test_case_get_item_info + negative_test_cases_get_item_info_incorrect_id


# Ручка {{baseUrl}}/api/1/statistic/:id - Получить статистику по айтем id

# Позитивный сценарий - передаем корректный id существующего объявления,
# которое было создано с параметром statistics
positive_test_case_get_item_statistics = [
    TestCase(test_name='GET_ITEM_STATISTICS_001',
             description='Переданы корректные данные - id существующего объявления',
             data=create_url(GET_ITEM_STATISTICS_PATH, current_item_id),
             expected_status_code=200,
             expected_schema=[])
]

# Позитивный сценарий - передаем корректный id существующего объявления,
# которое было создано без параметра statistics
positive_test_case_item_created_without_statistics = [
    TestCase(test_name='GET_ITEM_STATISTICS_002',
             description='Переданы корректные данные - id объявления, которое было создано без параметра statistics',
             data=create_url(GET_ITEM_STATISTICS_PATH, item_without_statistics_id),
             expected_status_code=200,
             expected_schema=[])
]

# Негативные сценарии - параметр id
negative_test_cases_get_item_statistics_incorrect_id = [
    TestCase(test_name='NEG_GET_ITEM_STATISTICS_001',
             description='Переданы некорректные данные - id несуществующего объявления',
             data=create_url(GET_ITEM_STATISTICS_PATH, 'ffffffff-ffff-ffff-ffff-ffffffffffff'),
             expected_status_code=404,
             expected_schema=incorrect_data_response),

    TestCase(test_name='NEG_GET_ITEM_STATISTICS_002',
             description='Переданы некорректные данные - пробел в качестве id объявления',
             data=create_url(GET_ITEM_STATISTICS_PATH, ' '),
             expected_status_code=400,
             expected_schema=incorrect_data_response),

    TestCase(test_name='NEG_GET_ITEM_STATISTICS_003',
             description='Переданы некорректные данные - отсутствуют "-" в id объявления',
             data=create_url(GET_ITEM_STATISTICS_PATH, get_copy_of(current_item_id).replace('-', '')),
             expected_status_code=400,
             expected_schema=incorrect_data_response)
]

# Собираем в один набор тест-кейсов для проверки параметра expected_status_code
test_cases_statistics_item_id = positive_test_case_get_item_statistics + \
                                positive_test_case_item_created_without_statistics + \
                                negative_test_cases_get_item_statistics_incorrect_id


# Ручка {{baseUrl}}/api/1/:sellerID/item - Получить все объявления по идентификатору продавца

# Позитивный сценарий - передаем корректный id существующего продавца
positive_test_case_get_seller_id_items = [
    TestCase(test_name='GET_SELLER_ITEMS_001',
             description='Переданы корректные данные - id существующего продавца',
             data=create_seller_items_url(GET_SELLER_ID_ITEMS, current_item_body['sellerID']),
             expected_status_code=200,
             expected_schema=[])
]

# Позитивный сценарий - продавец без объявлений
positive_test_case_seller_without_items = [
    TestCase(test_name='GET_SELLER_ITEMS_002',
             description='Переданы корректные данные - id продавца, у которого нет объявлений',
             data=create_seller_items_url(GET_SELLER_ID_ITEMS, 1234347777),
             expected_status_code=200,
             expected_schema=[])
]

# Негативные сценарии - параметр sellerID
negative_test_cases_get_seller_items = [
    TestCase(test_name='NEG_GET_SELLER_ITEMS_001',
             description='Переданы некорректные данные - sellerID = 0',
             data=create_seller_items_url(GET_SELLER_ID_ITEMS, 0),
             expected_status_code=400,
             expected_schema=incorrect_data_response),

    TestCase(test_name='NEG_GET_SELLER_ITEMS_002',
             description='Переданы некорректные данные - пробел в качестве sellerID',
             data=create_seller_items_url(GET_SELLER_ID_ITEMS, ' '),
             expected_status_code=400,
             expected_schema=incorrect_data_response)
]

# Собираем в один набор тест-кейсов для проверки параметра expected_status_code
test_cases_seller_id_items = positive_test_case_get_seller_id_items + positive_test_case_seller_without_items + \
                             negative_test_cases_get_seller_items
