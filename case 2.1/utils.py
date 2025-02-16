from configuration import CREATE_ITEM_PATH
from stand_request import post_new
from data import item_body, headers
import copy


def get_copy_of(data):
    return copy.deepcopy(data)


def change_item_body(param, new_data):
    new_item_body = get_copy_of(item_body)  # делаем глубокую копию исходного словаря тела запроса (файл data)
    if param == 'contacts' or param == 'likes' or param == 'viewCount':
        new_item_body['statistics'][param] = new_data
    else:
        new_item_body[param] = new_data
    return new_item_body


# Создание объявления для того, чтобы получить его id
def get_item_id_by_creating_item(body):
    return post_new(body, headers.copy(), CREATE_ITEM_PATH)


# Получение id объявления
def get_item_id(body):
    return get_item_id_by_creating_item(body).json()["status"][23:]


# Создание URL-адреса для запроса получения данных об объявлении
def create_url(end_path, item_id):
    return end_path + '/' + item_id


# Создание URL-адреса для запроса получения данных об объявлениях продавца
def create_seller_items_url(end_path, seller_id):
    return end_path.format(sellerID=seller_id)

