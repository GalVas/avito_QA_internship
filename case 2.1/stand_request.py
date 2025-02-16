from configuration import BASE_URL_SERVICE
import requests


def post_new(body, headers, end_path):
    return requests.post(BASE_URL_SERVICE + end_path,
                         json=body,
                         headers=headers)


def get_new(headers, end_path):
    return requests.get(BASE_URL_SERVICE + end_path,
                        headers=headers)