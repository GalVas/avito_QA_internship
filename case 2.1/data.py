headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

# тело запроса для создания объявления
item_body = {
    "sellerID": 1234345911,
    "name": "example",
    "price": 10,
    "statistics": {
        "contacts": 5,
        "likes": 2,
        "viewCount": 8
    }
}

# описание структуры JSON-ответа в случае успешного создания объявления
correct_data_response = {
    "type": "object",
    "properties": {
        "status": {"type": "string"}
    }
}

# JSON ответа (ошибки 4хх)
incorrect_data_response = {
    "type": "object",
    "properties": {
        "result": {
            "type": "object",
            "properties": {
                "message": {"type": "string"},
                "messages": {
                    "type": "object",
                    "properties": {
                        "additionalProp1": {"type": "string"},
                        "additionalProp2": {"type": "string"},
                        "additionalProp3": {"type": "string"},
                    }
                }
            },
            "required": ["message", "messages"]
        },
        "status": {"type": "string"}
    },
    "required": ["result", "status"]
}
