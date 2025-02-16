
# Найденные баги 

Багам присвоены следующие приоритеты: high, medium или low

**Для ручки POST /api/1/item - создание объявления**

| Параметр | Описание |
| --- | --- |
| id | BUG_CREATE_ITEM_01 |
| test_case_id | NEG_CREATE_ITEM_001 |
| Заголовок |Создание объявления возможно, если не передан обязательный параметр sellerID|
| Приоритет | high |
| Окружение | Адрес сервера: https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса не передать параметр sellerID, например: <br>{<br>⋅⋅⋅"name": "example", <br>⋅⋅⋅"price": 10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts": 5, <br>⋅⋅⋅⋅⋅⋅"likes": 2, <br>⋅⋅⋅⋅⋅⋅"viewCount": 8<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|
| Фактический результат | <br> 200 ОК <br> Успешное создание объявления <br> Тело ответа: "status": "Сохранили объявление - 74004e8b-cb32-4a67-9179-f05ff428a404"|

| Параметр | Описание |
| --- | --- |
| id | BUG_CREATE_ITEM_02 |
| test_case_id | NEG_CREATE_ITEM_002 |
| Заголовок |Создание объявления возможно, если не передан обязательный параметр name|
| Приоритет | medium |
| Окружение | Адрес сервера: https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса не передать параметр name, например: <br>{<br>⋅⋅⋅"sellerID":1234345989, <br>⋅⋅⋅"price":10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":5, <br>⋅⋅⋅⋅⋅⋅"likes":2, <br>⋅⋅⋅⋅⋅⋅"viewCount":8<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|
| Фактический результат | <br> 200 ОК <br> Успешное создание объявления <br> Тело ответа: "status": "Сохранили объявление - 74004e8b-cb32-4a67-9179-f05ff428a404"|

| Параметр | Описание |
| --- | --- |
| id | BUG_CREATE_ITEM_03 |
| test_case_id | NEG_CREATE_ITEM_003 |
| Заголовок |Создание объявления возможно, если не передан обязательный параметр price|
| Приоритет | medium |
| Окружение | Адрес сервера: https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса не передать параметр price, например: <br>{<br>⋅⋅⋅"sellerID":1234345989, <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":5, <br>⋅⋅⋅⋅⋅⋅"likes":2, <br>⋅⋅⋅⋅⋅⋅"viewCount":8<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|
| Фактический результат | <br> 200 ОК <br> Успешное создание объявления <br> Тело ответа: "status": "Сохранили объявление - 74004e8b-cb32-4a67-9179-f05ff428a404"|

| Параметр | Описание |
| --- | --- |
| id | BUG_CREATE_ITEM_04 |
| test_case_id | NEG_CREATE_ITEM_005 |
| Заголовок |Создание объявления возможно, если передано очень большое значение int для параметра sellerID|
| Приоритет | high |
| Окружение | Адрес сервера: https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса в параметр sellerID передать большое значение типа int, например: <br>{<br>⋅⋅⋅"sellerID":400000000000000, <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"price":10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":5, <br>⋅⋅⋅⋅⋅⋅"likes":2, <br>⋅⋅⋅⋅⋅⋅"viewCount":8<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|
| Фактический результат | <br> 200 ОК <br> Успешное создание объявления <br> Тело ответа: "status": "Сохранили объявление - 74004e8b-cb32-4a67-9179-f05ff428a404"|

| Параметр | Описание |
| --- | --- |
| id | BUG_CREATE_ITEM_05 |
| test_case_id | NEG_CREATE_ITEM_006 |
| Заголовок |Создание объявления возможно, если передано логически некорректное значение для параметра sellerID - 0|
| Приоритет | medium |
| Окружение | Адрес сервера: https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса в параметр sellerID передать 0, например: <br>{<br>⋅⋅⋅"sellerID":0, <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"price":10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":5, <br>⋅⋅⋅⋅⋅⋅"likes":2, <br>⋅⋅⋅⋅⋅⋅"viewCount":8<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|
| Фактический результат | <br> 200 ОК <br> Успешное создание объявления <br> Тело ответа: "status": "Сохранили объявление - 74004e8b-cb32-4a67-9179-f05ff428a404"|

| Параметр | Описание |
| --- | --- |
| id | BUG_CREATE_ITEM_06 |
| test_case_id | NEG_CREATE_ITEM_007 |
| Заголовок |Создание объявления возможно, если передано логически некорректное значение для параметра sellerID - -1|
| Приоритет | high |
| Окружение | Адрес сервера: https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса в параметр sellerID передать -1, например: <br>{<br>⋅⋅⋅"sellerID":-1, <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"price":10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":5, <br>⋅⋅⋅⋅⋅⋅"likes":2, <br>⋅⋅⋅⋅⋅⋅"viewCount":8<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|
| Фактический результат | <br> 200 ОК <br> Успешное создание объявления <br> Тело ответа: "status": "Сохранили объявление - 74004e8b-cb32-4a67-9179-f05ff428a404"|

| Параметр | Описание |
| --- | --- |
| id | BUG_CREATE_ITEM_07 |
| test_case_id | NEG_CREATE_ITEM_009 |
| Заголовок |Создание объявления возможно, если передано пустое значение для параметра name|
| Приоритет | medium |
| Окружение | Адрес сервера: https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса в параметр name передать "", например: <br>{<br>⋅⋅⋅"sellerID":1234345989, <br>⋅⋅⋅"name":"", <br>⋅⋅⋅"price":10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":5, <br>⋅⋅⋅⋅⋅⋅"likes":2, <br>⋅⋅⋅⋅⋅⋅"viewCount":8<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|
| Фактический результат | <br> 200 ОК <br> Успешное создание объявления <br> Тело ответа: "status": "Сохранили объявление - 74004e8b-cb32-4a67-9179-f05ff428a404"|

| Параметр | Описание |
| --- | --- |
| id | BUG_CREATE_ITEM_08 |
| test_case_id | NEG_CREATE_ITEM_011 |
| Заголовок |Создание объявления возможно, если передано очень большое значение int для параметра price|
| Приоритет | low |
| Окружение | Адрес сервера: https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса в параметр price передать большое значение типа int, например: <br>{<br>⋅⋅⋅"sellerID":1234345989, <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"price":400000000000000, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":5, <br>⋅⋅⋅⋅⋅⋅"likes":2, <br>⋅⋅⋅⋅⋅⋅"viewCount":8<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|
| Фактический результат | <br> 200 ОК <br> Успешное создание объявления <br> Тело ответа: "status": "Сохранили объявление - 74004e8b-cb32-4a67-9179-f05ff428a404"|

| Параметр | Описание |
| --- | --- |
| id | BUG_CREATE_ITEM_09 |
| test_case_id | NEG_CREATE_ITEM_012 |
| Заголовок |Создание объявления возможно, если передано логически некорректное значение для параметра price - 0|
| Приоритет | low |
| Окружение | Адрес сервера: https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса в параметр price передать 0, например: <br>{<br>⋅⋅⋅"sellerID":1234345989, <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"price":0, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":5, <br>⋅⋅⋅⋅⋅⋅"likes":2, <br>⋅⋅⋅⋅⋅⋅"viewCount":8<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|
| Фактический результат | <br> 200 ОК <br> Успешное создание объявления <br> Тело ответа: "status": "Сохранили объявление - 74004e8b-cb32-4a67-9179-f05ff428a404"|

| Параметр | Описание |
| --- | --- |
| id | BUG_CREATE_ITEM_10 |
| test_case_id | NEG_CREATE_ITEM_013 |
| Заголовок |Создание объявления возможно, если передано логически некорректное значение для параметра price - -1|
| Приоритет | medium |
| Окружение | Адрес сервера: https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса в параметр price передать -1, например: <br>{<br>⋅⋅⋅"sellerID":1234345989, <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"price":-1, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":5, <br>⋅⋅⋅⋅⋅⋅"likes":2, <br>⋅⋅⋅⋅⋅⋅"viewCount":8<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|
| Фактический результат | <br> 200 ОК <br> Успешное создание объявления <br> Тело ответа: "status": "Сохранили объявление - 74004e8b-cb32-4a67-9179-f05ff428a404"|

| Параметр | Описание |
| --- | --- |
| id | BUG_CREATE_ITEM_11 |
| test_case_id | NEG_CREATE_ITEM_017 |
| Заголовок |Создание объявления возможно, если передано очень большое значение int для параметра contacts|
| Приоритет | low |
| Окружение | Адрес сервера: https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса в параметр contacts передать большое значение типа int, например: <br>{<br>⋅⋅⋅"sellerID":1234345989, <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"price":10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":400000000000000, <br>⋅⋅⋅⋅⋅⋅"likes":2, <br>⋅⋅⋅⋅⋅⋅"viewCount":8<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|
| Фактический результат | <br> 200 ОК <br> Успешное создание объявления <br> Тело ответа: "status": "Сохранили объявление - 74004e8b-cb32-4a67-9179-f05ff428a404"|

| Параметр | Описание |
| --- | --- |
| id | BUG_CREATE_ITEM_12 |
| test_case_id | NEG_CREATE_ITEM_018 |
| Заголовок |Создание объявления возможно, если передано логически некорректное значение для параметра contacts - -1|
| Приоритет | medium |
| Окружение | Адрес сервера: https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса в параметр contacts передать -1, например: <br>{<br>⋅⋅⋅"sellerID":1234345989, <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"price":10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":-1, <br>⋅⋅⋅⋅⋅⋅"likes":2, <br>⋅⋅⋅⋅⋅⋅"viewCount":8<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|
| Фактический результат | <br> 200 ОК <br> Успешное создание объявления <br> Тело ответа: "status": "Сохранили объявление - 74004e8b-cb32-4a67-9179-f05ff428a404"|

| Параметр | Описание |
| --- | --- |
| id | BUG_CREATE_ITEM_13 |
| test_case_id | NEG_CREATE_ITEM_020 |
| Заголовок |Создание объявления возможно, если передано очень большое значение int для параметра likes|
| Приоритет | low |
| Окружение | Адрес сервера: https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса в параметр likes передать большое значение типа int, например: <br>{<br>⋅⋅⋅"sellerID":1234345989, <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"price":10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":5, <br>⋅⋅⋅⋅⋅⋅"likes":400000000000000, <br>⋅⋅⋅⋅⋅⋅"viewCount":8<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|
| Фактический результат | <br> 200 ОК <br> Успешное создание объявления <br> Тело ответа: "status": "Сохранили объявление - 74004e8b-cb32-4a67-9179-f05ff428a404"|

| Параметр | Описание |
| --- | --- |
| id | BUG_CREATE_ITEM_14 |
| test_case_id | NEG_CREATE_ITEM_021 |
| Заголовок |Создание объявления возможно, если передано логически некорректное значение для параметра likes - -1|
| Приоритет | medium |
| Окружение | Адрес сервера: https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса в параметр likes передать -1, например: <br>{<br>⋅⋅⋅"sellerID":1234345989, <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"price":10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":5, <br>⋅⋅⋅⋅⋅⋅"likes":-1, <br>⋅⋅⋅⋅⋅⋅"viewCount":8<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|
| Фактический результат | <br> 200 ОК <br> Успешное создание объявления <br> Тело ответа: "status": "Сохранили объявление - 74004e8b-cb32-4a67-9179-f05ff428a404"|

| Параметр | Описание |
| --- | --- |
| id | BUG_CREATE_ITEM_15 |
| test_case_id | NEG_CREATE_ITEM_023 |
| Заголовок |Создание объявления возможно, если передано очень большое значение int для параметра viewCount|
| Приоритет | low |
| Окружение | Адрес сервера: https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса в параметр viewCount передать большое значение типа int, например: <br>{<br>⋅⋅⋅"sellerID":1234345989, <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"price":10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":5, <br>⋅⋅⋅⋅⋅⋅"likes":2, <br>⋅⋅⋅⋅⋅⋅"viewCount":400000000000000<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|
| Фактический результат | <br> 200 ОК <br> Успешное создание объявления <br> Тело ответа: "status": "Сохранили объявление - 74004e8b-cb32-4a67-9179-f05ff428a404"|

| Параметр | Описание |
| --- | --- |
| id | BUG_CREATE_ITEM_16|
| test_case_id | NEG_CREATE_ITEM_024|
| Заголовок |Создание объявления возможно, если передано логически некорректное значение для параметра viewCount - -1|
| Приоритет | medium |
| Окружение | Адрес сервера: https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса в параметр viewCount передать -1, например: <br>{<br>⋅⋅⋅"sellerID":1234345989, <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"price":10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":5, <br>⋅⋅⋅⋅⋅⋅"likes":2, <br>⋅⋅⋅⋅⋅⋅"viewCount":-1<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|
| Фактический результат | <br> 200 ОК <br> Успешное создание объявления <br> Тело ответа: "status": "Сохранили объявление - 74004e8b-cb32-4a67-9179-f05ff428a404"|

| Параметр | Описание |
| --- | --- |
| id | BUG_CREATE_ITEM_17|
| test_case_id | NEG_CREATE_ITEM_015|
| Заголовок |Создание объявления возможно, если передан пустой параметр statistics|
| Приоритет | high |
| Окружение | Адрес сервера: https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса передать пустой параметр statistics, например: <br>{<br>⋅⋅⋅"sellerID":1234345989, <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"price":10, <br>⋅⋅⋅"statistics": {}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|
| Фактический результат | <br> 200 ОК <br> Успешное создание объявления <br> Тело ответа: "status": "Сохранили объявление - 74004e8b-cb32-4a67-9179-f05ff428a404"|

**Для ручки GET /api/1/item/{id} - получение объявления по его идентификатору**

| Параметр | Описание |
| --- | --- |
| id | BUG_GET_ITEM_INFO_1|
| test_case_id | NEG_GET_ITEM_INFO_003|
| Заголовок |Получение объявления по его id возможно, если передан некорректный id - отсутствуют "-"|
| Приоритет | low |
| Окружение | Адрес сервера: https://qa-internship.avito.com |
| Предусловие | Создать объявление (POST /api/1/item):  <br>{<br>⋅⋅⋅"sellerID": 1234345989, <br>⋅⋅⋅"name": "example", <br>⋅⋅⋅"price": 10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts": 5, <br>⋅⋅⋅⋅⋅⋅"likes": 2, <br>⋅⋅⋅⋅⋅⋅"viewCount": 8<br>⋅⋅⋅}<br>}|
| Шаги для воспроизведения | Отправить GET на возможность получения объявления по его id - '/api/1/item/{id}', в url параметр передать id ранее созданного объявления без "-", например: '5596170f55c5441182e2e5acdee54854'|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|
| Фактический результат | <br> 200 ОК <br>{<br>⋅⋅⋅"ID":"5596170f-55c5-4411-82e2-e5acdee54854"<br>⋅⋅⋅"sellerID": 1234345989, <br>⋅⋅⋅"name": "example", <br>⋅⋅⋅"price": 10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts": 5, <br>⋅⋅⋅⋅⋅⋅"likes": 2, <br>⋅⋅⋅⋅⋅⋅"viewCount": 8<br>⋅⋅⋅}<br>} <br>Можно получить информацию об объявлении|

| Параметр | Описание |
| --- | --- |
| id | BUG_GET_ITEM_INFO_2|
| test_case_id | NEG_GET_ITEM_INFO_001|
| Заголовок |Некорректный тип данных параметра messages в теле ответа при передаче id несуществующего объявления|
| Приоритет | medium |
| Окружение | Адрес сервера: https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить GET на возможность получения объявления по его id - '/api/1/item/{id}', в url параметр передать id несуществующего объявления, например: 'ffffffff-ffff-ffff-ffff-ffffffffffff'|
| Ожидаемый результат | <br> 404 Not Found <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|
| Фактический результат | <br> 404 Not Found <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "item ffffffff-ffff-ffff-ffff-ffffffffffff not found",<br>⋅⋅⋅⋅⋅⋅"messages": None <br>⋅⋅⋅},<br>⋅⋅⋅"status": "404"<br>} <br> Параметр messages возвращает None, вместо {}|

| Параметр | Описание |
| --- | --- |
| id | BUG_GET_ITEM_INFO_3|
| test_case_id | GET_ITEM_INFO_001|
| Заголовок |Некорректное значение параметра name в теле ответа при отправке запроса на получение объявления|
| Приоритет | high |
| Окружение | Адрес сервера: https://qa-internship.avito.com |
| Предусловие | Создать объявление (POST /api/1/item):  <br>{<br>⋅⋅⋅"sellerID": 1234345989, <br>⋅⋅⋅"name": "example", <br>⋅⋅⋅"price": 10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts": 5, <br>⋅⋅⋅⋅⋅⋅"likes": 2, <br>⋅⋅⋅⋅⋅⋅"viewCount": 8<br>⋅⋅⋅}<br>}|
| Шаги для воспроизведения | Отправить GET на возможность получения объявления по его id - '/api/1/item/{id}', в url параметр передать id существующего ранее созданного объявления, например: '5596170f-55c5-4411-82e2-e5acdee54854'|
| Ожидаемый результат | <br> 200 ОК <br>{<br>⋅⋅⋅"sellerID": 1234345989, <br>⋅⋅⋅"name": "example", <br>⋅⋅⋅"price": 10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts": 5, <br>⋅⋅⋅⋅⋅⋅"likes": 2, <br>⋅⋅⋅⋅⋅⋅"viewCount": 8<br>⋅⋅⋅}<br>}|
| Фактический результат | <br> 200 ОК <br>{<br>⋅⋅⋅"ID":"5596170f-55c5-4411-82e2-e5acdee54854"<br>⋅⋅⋅"sellerID": 1234345989, <br>⋅⋅⋅"name": "dsdsd", <br>⋅⋅⋅"price": 10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts": 5, <br>⋅⋅⋅⋅⋅⋅"likes": 2, <br>⋅⋅⋅⋅⋅⋅"viewCount": 8<br>⋅⋅⋅}<br>} <br> Параметр name не совпадает|

**Для ручки GET /api/1/statistic/{id} - получение статистики объявления по его идентификатору**

| Параметр | Описание |
| --- | --- |
| id | BUG_GET_ITEM_STAT_1|
| test_case_id | NEG_GET_ITEM_STATISTICS_003|
| Заголовок |Получение статистики объявления по его id возможно, если передан некорректный id - отсутствуют "-"|
| Приоритет | low |
| Окружение | Адрес сервера: https://qa-internship.avito.com |
| Предусловие | Создать объявление (POST /api/1/item):  <br>{<br>⋅⋅⋅"sellerID": 1234345989, <br>⋅⋅⋅"name": "example", <br>⋅⋅⋅"price": 10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts": 5, <br>⋅⋅⋅⋅⋅⋅"likes": 2, <br>⋅⋅⋅⋅⋅⋅"viewCount": 8<br>⋅⋅⋅}<br>}|
| Шаги для воспроизведения | Отправить GET на возможность получения статистики объявления по его id - '/api/1/statistic/{id}', в url параметр передать id ранее созданного объявления без "-", например: '5596170f55c5441182e2e5acdee54854'|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|
| Фактический результат | <br> 200 ОК <br>{<br>⋅⋅⋅"sellerID": 1234345989, <br>⋅⋅⋅"name": "example", <br>⋅⋅⋅"price": 10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts": 5, <br>⋅⋅⋅⋅⋅⋅"likes": 2, <br>⋅⋅⋅⋅⋅⋅"viewCount": 8<br>⋅⋅⋅}<br>} <br>Можно получить статистику объявления|

| Параметр | Описание |
| --- | --- |
| id | BUG_GET_ITEM_STAT_2|
| test_case_id | NEG_GET_ITEM_STATISTICS_001|
| Заголовок |Некорректный тип данных параметра messages в теле ответа при передаче id несуществующего объявления|
| Приоритет | medium |
| Окружение | Адрес сервера: https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить GET на возможность получения статистики объявления по его id - '/api/1/item/{id}', в url параметр передать id несуществующего объявления, например: 'ffffffff-ffff-ffff-ffff-ffffffffffff'|
| Ожидаемый результат | <br> 404 Not Found <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|
| Фактический результат | <br> 404 Not Found <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "item ffffffff-ffff-ffff-ffff-ffffffffffff not found",<br>⋅⋅⋅⋅⋅⋅"messages": None <br>⋅⋅⋅},<br>⋅⋅⋅"status": "404"<br>} <br>Параметр messages возвращает None, вместо {}|

| Параметр | Описание |
| --- | --- |
| id |BUG_GET_ITEM_STAT_3|
| test_case_id | GET_ITEM_STATISTICS_001|
| Заголовок |Некорректное значение параметра likes в теле ответа при отправке запроса на получение статистики объявления|
| Приоритет | medium |
| Окружение | Адрес сервера: https://qa-internship.avito.com |
| Предусловие | Создать объявление (POST /api/1/item):  <br>{<br>⋅⋅⋅"sellerID": 1234345989, <br>⋅⋅⋅"name": "example", <br>⋅⋅⋅"price": 10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts": 5, <br>⋅⋅⋅⋅⋅⋅"likes": 2, <br>⋅⋅⋅⋅⋅⋅"viewCount": 8<br>⋅⋅⋅}<br>}|
| Шаги для воспроизведения | Отправить GET на возможность получения статистики объявления по его id - '/api/1/statistic/{id}', в url параметр передать id существующего ранее созданного объявления, например: '5596170f-55c5-4411-82e2-e5acdee54854'|
| Ожидаемый результат | <br> 200 ОК <br>[<br>{<br>⋅⋅⋅"contacts": 5, <br>⋅⋅⋅"likes": 2, <br>⋅⋅⋅"viewCount": 8<br>}<br>]|
| Фактический результат | <br> 200 ОК <br>[<br>⋅⋅⋅{<br>⋅⋅⋅⋅⋅⋅"contacts": 5, <br>⋅⋅⋅⋅⋅⋅"likes": 4, <br>⋅⋅⋅⋅⋅⋅"viewCount": 12<br>⋅⋅⋅}<br>] <br> Параметр likes не совпадает - увеличивается в два раза|

| Параметр | Описание |
| --- | --- |
| id |BUG_GET_ITEM_STAT_4|
| test_case_id | GET_ITEM_STATISTICS_001|
| Заголовок |Некорректное значение параметра viewCount в теле ответа при отправке запроса на получение статистики объявления|
| Приоритет | low |
| Окружение | Адрес сервера: https://qa-internship.avito.com |
| Предусловие | Создать объявление (POST /api/1/item):  <br>{<br>⋅⋅⋅"sellerID": 1234345989, <br>⋅⋅⋅"name": "example", <br>⋅⋅⋅"price": 10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts": 5, <br>⋅⋅⋅⋅⋅⋅"likes": 2, <br>⋅⋅⋅⋅⋅⋅"viewCount": 8<br>⋅⋅⋅}<br>}|
| Шаги для воспроизведения | Отправить GET на возможность получения статистики объявления по его id - '/api/1/statistic/{id}', в url параметр передать id существующего ранее созданного объявления, например: '5596170f-55c5-4411-82e2-e5acdee54854'|
| Ожидаемый результат | <br> 200 ОК <br>[<br>{<br>⋅⋅⋅"contacts": 5, <br>⋅⋅⋅"likes": 2, <br>⋅⋅⋅"viewCount": 8<br>}<br>]|
| Фактический результат | <br> 200 ОК <br>[<br>⋅⋅⋅{<br>⋅⋅⋅⋅⋅⋅"contacts": 5, <br>⋅⋅⋅⋅⋅⋅"likes": 4, <br>⋅⋅⋅⋅⋅⋅"viewCount": 12<br>⋅⋅⋅}<br>] <br> Параметр viewCount не совпадает - увеличивается на 4|

**Для ручки GET /api/1/{sellerID}/item - получение всех объявлений по идентификатору продавца**

| Параметр | Описание |
| --- | --- |
| id |BUG_GET_SELLER_ITEMS_1|
| test_case_id | GET_SELLER_ITEMS_001|
| Заголовок |Некорректное значение параметра ID в теле ответа при отправке запроса на получение всех объявлений продавца|
| Приоритет | high |
| Окружение | Адрес сервера: https://qa-internship.avito.com |
| Предусловие | Создать объявление (POST /api/1/item):  <br>{<br>⋅⋅⋅"sellerID": 1234345777, <br>⋅⋅⋅"name": "example", <br>⋅⋅⋅"price": 10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts": 5, <br>⋅⋅⋅⋅⋅⋅"likes": 2, <br>⋅⋅⋅⋅⋅⋅"viewCount": 8<br>⋅⋅⋅}<br>} <br> Запомнить id объявления (например, это 5596170f-55c5-4411-82e2-e5acdee54854)|
| Шаги для воспроизведения | Отправить GET на возможность получения списка всех объявлений продавца по его id - '/api/1/{sellerID}/item', в url параметр передать id существующего продавца, для которого ранее создавали объявление, например: '1234345777'|
| Ожидаемый результат | <br> 200 ОК <br>{<br>⋅⋅⋅"ID":"5596170f-55c5-4411-82e2-e5acdee54854", <br>⋅⋅⋅"sellerID": 1234345777, <br>⋅⋅⋅"name": "example", <br>⋅⋅⋅"price": 10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts": 5, <br>⋅⋅⋅⋅⋅⋅"likes": 2, <br>⋅⋅⋅⋅⋅⋅"viewCount": 8<br>⋅⋅⋅}<br>}|
| Фактический результат | <br> 200 ОК <br>{<br>⋅⋅⋅"ID":"example", <br>⋅⋅⋅"sellerID": 1234345777, <br>⋅⋅⋅"name": "5596170f-55c5-4411-82e2-e5acdee54854", <br>⋅⋅⋅"price": 10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts": 5, <br>⋅⋅⋅⋅⋅⋅"likes": 2, <br>⋅⋅⋅⋅⋅⋅"viewCount": 8<br>⋅⋅⋅}<br>} <br> Параметр ID не совпадает - сохраняются данные из параметра name|

| Параметр | Описание |
| --- | --- |
| id |BUG_GET_SELLER_ITEMS_2|
| test_case_id | GET_SELLER_ITEMS_001|
| Заголовок |Некорректное значение параметра name в теле ответа при отправке запроса на получение всех объявлений продавца|
| Приоритет | high |
| Окружение | Адрес сервера: https://qa-internship.avito.com |
| Предусловие | Создать объявление (POST /api/1/item):  <br>{<br>⋅⋅⋅"sellerID": 1234345777, <br>⋅⋅⋅"name": "example", <br>⋅⋅⋅"price": 10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts": 5, <br>⋅⋅⋅⋅⋅⋅"likes": 2, <br>⋅⋅⋅⋅⋅⋅"viewCount": 8<br>⋅⋅⋅}<br>} <br> Запомнить id объявления (например, это 5596170f-55c5-4411-82e2-e5acdee54854)|
| Шаги для воспроизведения | Отправить GET на возможность получения списка всех объявлений продавца по его id - '/api/1/{sellerID}/item', в url параметр передать id существующего продавца, для которого ранее создавали объявление, например: '1234345777'|
| Ожидаемый результат | <br> 200 ОК <br>{<br>⋅⋅⋅"ID":"5596170f-55c5-4411-82e2-e5acdee54854", <br>⋅⋅⋅"sellerID": 1234345777, <br>⋅⋅⋅"name": "example", <br>⋅⋅⋅"price": 10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts": 5, <br>⋅⋅⋅⋅⋅⋅"likes": 2, <br>⋅⋅⋅⋅⋅⋅"viewCount": 8<br>⋅⋅⋅}<br>}|
| Фактический результат | <br> 200 ОК <br>{<br>⋅⋅⋅"ID":"example", <br>⋅⋅⋅"sellerID": 1234345777, <br>⋅⋅⋅"name": "5596170f-55c5-4411-82e2-e5acdee54854", <br>⋅⋅⋅"price": 10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts": 5, <br>⋅⋅⋅⋅⋅⋅"likes": 2, <br>⋅⋅⋅⋅⋅⋅"viewCount": 8<br>⋅⋅⋅}<br>} <br> Параметр name не совпадает - сохраняются данные из параметра ID|

