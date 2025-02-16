
# Тесты на проверку создания объявления, получения объявления по его идентификатору, статистики объявления и всех объявлений по идентификатору продавца в Avito qa-internship с помощью API Avito

#Тест-кейсы для ручки POST /api/1/item - создание объявления

| Параметр | Описание |
| --- | --- |
| id | CREATE_ITEM_001 |
| Заголовок | Создание объявления возможно, если переданы корректные данные для параметров sellerID (1234345989), name ("example"), price (10), statistics (contacts (5), likes (2), viewCount (8))|
| Адрес сервера | https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в тело запроса передать корректные данные для параметров, например: sellerID (1234345989), name ("example"), price (10), statistics (contacts (5), likes (2), viewCount (8))  |
| Ожидаемый результат | <br> 200 OK <br> Ошибок в структуре ответа нет: {"status": "string"} <br> Ответ содержит информацию о создании объявления, например: "status": "Сохранили объявление - 5596170f-55c5-4411-82e2-e5acdee54854"|

| Параметр | Описание |
| --- | --- |
| id | CREATE_ITEM_002 |
| Заголовок | Создание объявления возможно, если переданы корректные данные для параметров sellerID, name, price и отсутствует необязательное поле statistics|
| Адрес сервера | https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в тело запроса передать корректные данные для параметров, например: <br>{<br>⋅⋅⋅"sellerID":1234345989, <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"price":10<br>}|
| Ожидаемый результат | <br> 200 OK <br> Ошибок в структуре ответа нет: {"status": "string"} <br> Ответ содержит информацию о создании объявления, например: "status": "Сохранили объявление - 5596170f-55c5-4411-82e2-e5acdee54854"|

| Параметр | Описание |
| --- | --- |
| id | CREATE_ITEM_003 |
| Заголовок | Создание объявления возможно, если переданы корректные данные для параметров sellerID, name, price, likes, viewCount и параметр contacts = 0|
| Адрес сервера | https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в тело запроса передать корректные данные для параметров, параметр contacts = 0, например: <br>{<br>⋅⋅⋅"sellerID":1234345989, <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"price":10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":0, <br>⋅⋅⋅⋅⋅⋅"likes":2, <br>⋅⋅⋅⋅⋅⋅"viewCount":8<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 200 OK <br> Ошибок в структуре ответа нет: {"status": "string"} <br> Ответ содержит информацию о создании объявления, например: "status": "Сохранили объявление - 5596170f-55c5-4411-82e2-e5acdee54854"|

| Параметр | Описание |
| --- | --- |
| id | CREATE_ITEM_004 |
| Заголовок | Создание объявления возможно, если переданы корректные данные для параметров sellerID, name, price, contacts, viewCount и параметр likes = 0|
| Адрес сервера | https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в тело запроса передать корректные данные для параметров, параметр likes = 0, например: <br>{<br>⋅⋅⋅"sellerID":1234345989, <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"price":10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":5, <br>⋅⋅⋅⋅⋅⋅"likes":0, <br>⋅⋅⋅⋅⋅⋅"viewCount":8<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 200 OK <br> Ошибок в структуре ответа нет: {"status": "string"} <br> Ответ содержит информацию о создании объявления, например: "status": "Сохранили объявление - 5596170f-55c5-4411-82e2-e5acdee54854"|

| Параметр | Описание |
| --- | --- |
| id | CREATE_ITEM_005 |
| Заголовок | Создание объявления возможно, если переданы корректные данные для параметров sellerID, name, price, contacts, likes и параметр viewCount = 0|
| Адрес сервера | https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в тело запроса передать корректные данные для параметров, параметр viewCount = 0, например: <br>{<br>⋅⋅⋅"sellerID":1234345989, <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"price":10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":5, <br>⋅⋅⋅⋅⋅⋅"likes":2, <br>⋅⋅⋅⋅⋅⋅"viewCount":0<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 200 OK <br> Ошибок в структуре ответа нет: {"status": "string"} <br> Ответ содержит информацию о создании объявления, например: "status": "Сохранили объявление - 5596170f-55c5-4411-82e2-e5acdee54854"|

# Негативные проверки 
**Тестовый набор - не переданы обязательные параметры**

| Параметр | Описание |
| --- | --- |
| id | NEG_CREATE_ITEM_001 |
| Заголовок | Создание объявления невозможно, если не передан обязательный параметр sellerID|
| Адрес сервера | https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса не передать параметр sellerID, например: <br>{<br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"price":10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":5, <br>⋅⋅⋅⋅⋅⋅"likes":2, <br>⋅⋅⋅⋅⋅⋅"viewCount":8<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|

| Параметр | Описание |
| --- | --- |
| id | NEG_CREATE_ITEM_002 |
| Заголовок | Создание объявления невозможно, если не передан обязательный параметр name|
| Адрес сервера | https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса не передать параметр name, например: <br>{<br>⋅⋅⋅"sellerID":1234345989, <br>⋅⋅⋅"price":10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":5, <br>⋅⋅⋅⋅⋅⋅"likes":2, <br>⋅⋅⋅⋅⋅⋅"viewCount":8<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|

| Параметр | Описание |
| --- | --- |
| id | NEG_CREATE_ITEM_003 |
| Заголовок | Создание объявления невозможно, если не передан обязательный параметр price|
| Адрес сервера | https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса не передать параметр price, например: <br>{<br>⋅⋅⋅"sellerID":1234345989, <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":5, <br>⋅⋅⋅⋅⋅⋅"likes":2, <br>⋅⋅⋅⋅⋅⋅"viewCount":8<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|

**Тестовый набор - негативные проверки для параметра sellerID**

| Параметр | Описание |
| --- | --- |
| id | NEG_CREATE_ITEM_004 |
| Заголовок | Создание объявления невозможно, если передан недопустимый тип данных для параметра sellerID: str|
| Адрес сервера | https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса передать тип данных str в параметр sellerID, например: <br>{<br>⋅⋅⋅"sellerID":"1234345989", <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"price":10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":5, <br>⋅⋅⋅⋅⋅⋅"likes":2, <br>⋅⋅⋅⋅⋅⋅"viewCount":8<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|

| Параметр | Описание |
| --- | --- |
| id | NEG_CREATE_ITEM_005 |
| Заголовок | Создание объявления невозможно, если передано очень большое значение int для параметра sellerID|
| Адрес сервера | https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса в параметр sellerID передать большое значение типа int, например: <br>{<br>⋅⋅⋅"sellerID":400000000000000, <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"price":10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":5, <br>⋅⋅⋅⋅⋅⋅"likes":2, <br>⋅⋅⋅⋅⋅⋅"viewCount":8<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|

| Параметр | Описание |
| --- | --- |
| id | NEG_CREATE_ITEM_006 |
| Заголовок | Создание объявления невозможно, если передано логически некорректное значение для параметра sellerID - 0|
| Адрес сервера | https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса в параметр sellerID передать 0, например: <br>{<br>⋅⋅⋅"sellerID":0, <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"price":10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":5, <br>⋅⋅⋅⋅⋅⋅"likes":2, <br>⋅⋅⋅⋅⋅⋅"viewCount":8<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|

| Параметр | Описание |
| --- | --- |
| id | NEG_CREATE_ITEM_007 |
| Заголовок | Создание объявления невозможно, если передано логически некорректное значение для параметра sellerID - -1|
| Адрес сервера | https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса в параметр sellerID передать -1, например: <br>{<br>⋅⋅⋅"sellerID":-1, <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"price":10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":5, <br>⋅⋅⋅⋅⋅⋅"likes":2, <br>⋅⋅⋅⋅⋅⋅"viewCount":8<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|

**Тестовый набор - негативные проверки для параметра name**

| Параметр | Описание |
| --- | --- |
| id | NEG_CREATE_ITEM_008 |
| Заголовок | Создание объявления невозможно, если передан недопустимый тип данных для параметра name: int|
| Адрес сервера | https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса в параметр name передать 1111111111, например: <br>{<br>⋅⋅⋅"sellerID":1234345989, <br>⋅⋅⋅"name":1111111111, <br>⋅⋅⋅"price":10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":5, <br>⋅⋅⋅⋅⋅⋅"likes":2, <br>⋅⋅⋅⋅⋅⋅"viewCount":8<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|

| Параметр | Описание |
| --- | --- |
| id | NEG_CREATE_ITEM_009 |
| Заголовок | Создание объявления невозможно, если передано пустое значение для параметра name|
| Адрес сервера | https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса в параметр name передать "", например: <br>{<br>⋅⋅⋅"sellerID":1234345989, <br>⋅⋅⋅"name":"", <br>⋅⋅⋅"price":10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":5, <br>⋅⋅⋅⋅⋅⋅"likes":2, <br>⋅⋅⋅⋅⋅⋅"viewCount":8<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|

**Тестовый набор - негативные проверки для параметра price**

| Параметр | Описание |
| --- | --- |
| id | NEG_CREATE_ITEM_010 |
| Заголовок | Создание объявления невозможно, если передан недопустимый тип данных для параметра price: str|
| Адрес сервера | https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса передать тип данных str в параметр price, например: <br>{<br>⋅⋅⋅"sellerID":1234345989, <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"price":"12345", <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":5, <br>⋅⋅⋅⋅⋅⋅"likes":2, <br>⋅⋅⋅⋅⋅⋅"viewCount":8<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|

| Параметр | Описание |
| --- | --- |
| id | NEG_CREATE_ITEM_011 |
| Заголовок | Создание объявления невозможно, если передано очень большое значение int для параметра price|
| Адрес сервера | https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса в параметр price передать большое значение типа int, например: <br>{<br>⋅⋅⋅"sellerID":1234345989, <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"price":400000000000000, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":5, <br>⋅⋅⋅⋅⋅⋅"likes":2, <br>⋅⋅⋅⋅⋅⋅"viewCount":8<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|

| Параметр | Описание |
| --- | --- |
| id | NEG_CREATE_ITEM_012 |
| Заголовок | Создание объявления невозможно, если передано логически некорректное значение для параметра price - 0|
| Адрес сервера | https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса в параметр price передать 0, например: <br>{<br>⋅⋅⋅"sellerID":1234345989, <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"price":0, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":5, <br>⋅⋅⋅⋅⋅⋅"likes":2, <br>⋅⋅⋅⋅⋅⋅"viewCount":8<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|

| Параметр | Описание |
| --- | --- |
| id | NEG_CREATE_ITEM_013 |
| Заголовок | Создание объявления невозможно, если передано логически некорректное значение для параметра price - -1|
| Адрес сервера | https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса в параметр price передать -1, например: <br>{<br>⋅⋅⋅"sellerID":1234345989, <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"price":-1, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":5, <br>⋅⋅⋅⋅⋅⋅"likes":2, <br>⋅⋅⋅⋅⋅⋅"viewCount":8<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|

**Тестовый набор - негативные проверки для параметра statistics**

| Параметр | Описание |
| --- | --- |
| id | NEG_CREATE_ITEM_014 |
| Заголовок | Создание объявления невозможно,  если передан недопустимый тип данных для параметра statistics: list|
| Адрес сервера | https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса передать тип данных list в параметр statistics, например: <br>{<br>⋅⋅⋅"sellerID":1234345989, <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"price":10, <br>⋅⋅⋅"statistics": [<br>⋅⋅⋅⋅⋅⋅"contacts":5, <br>⋅⋅⋅⋅⋅⋅"likes":2, <br>⋅⋅⋅⋅⋅⋅"viewCount":8<br>⋅⋅⋅]<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|

| Параметр | Описание |
| --- | --- |
| id | NEG_CREATE_ITEM_015 |
| Заголовок | Создание объявления невозможно,  если передан пустой параметр statistics|
| Адрес сервера | https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса передать пустой параметр statistics, например: <br>{<br>⋅⋅⋅"sellerID":1234345989, <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"price":10, <br>⋅⋅⋅"statistics": {}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|

**Тестовый набор - негативные проверки для параметра contacts**

| Параметр | Описание |
| --- | --- |
| id | NEG_CREATE_ITEM_016 |
| Заголовок | Создание объявления невозможно, если передан недопустимый тип данных для параметра contacts: str|
| Адрес сервера | https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса передать тип данных str в параметр contacts, например: <br>{<br>⋅⋅⋅"sellerID":1234345989, <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"price":10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":"12345", <br>⋅⋅⋅⋅⋅⋅"likes":2, <br>⋅⋅⋅⋅⋅⋅"viewCount":8<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|

| Параметр | Описание |
| --- | --- |
| id | NEG_CREATE_ITEM_017 |
| Заголовок | Создание объявления невозможно, если передано очень большое значение int для параметра contacts|
| Адрес сервера | https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса в параметр contacts передать большое значение типа int, например: <br>{<br>⋅⋅⋅"sellerID":1234345989, <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"price":10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":400000000000000, <br>⋅⋅⋅⋅⋅⋅"likes":2, <br>⋅⋅⋅⋅⋅⋅"viewCount":8<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|

| Параметр | Описание |
| --- | --- |
| id | NEG_CREATE_ITEM_018 |
| Заголовок | Создание объявления невозможно, если передано логически некорректное значение для параметра contacts - -1|
| Адрес сервера | https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса в параметр contacts передать -1, например: <br>{<br>⋅⋅⋅"sellerID":1234345989, <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"price":10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":-1, <br>⋅⋅⋅⋅⋅⋅"likes":2, <br>⋅⋅⋅⋅⋅⋅"viewCount":8<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|

**Тестовый набор - негативные проверки для параметра likes**

| Параметр | Описание |
| --- | --- |
| id | NEG_CREATE_ITEM_019 |
| Заголовок | Создание объявления невозможно, если передан недопустимый тип данных для параметра likes: str|
| Адрес сервера | https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса передать тип данных str в параметр likes, например: <br>{<br>⋅⋅⋅"sellerID":1234345989, <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"price":10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":5, <br>⋅⋅⋅⋅⋅⋅"likes":"123", <br>⋅⋅⋅⋅⋅⋅"viewCount":8<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|

| Параметр | Описание |
| --- | --- |
| id | NEG_CREATE_ITEM_020 |
| Заголовок | Создание объявления невозможно, если передано очень большое значение int для параметра likes|
| Адрес сервера | https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса в параметр likes передать большое значение типа int, например: <br>{<br>⋅⋅⋅"sellerID":1234345989, <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"price":10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":5, <br>⋅⋅⋅⋅⋅⋅"likes":400000000000000, <br>⋅⋅⋅⋅⋅⋅"viewCount":8<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|

| Параметр | Описание |
| --- | --- |
| id | NEG_CREATE_ITEM_021 |
| Заголовок | Создание объявления невозможно, если передано логически некорректное значение для параметра likes - -1|
| Адрес сервера | https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса в параметр likes передать -1, например: <br>{<br>⋅⋅⋅"sellerID":1234345989, <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"price":10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":5, <br>⋅⋅⋅⋅⋅⋅"likes":-1, <br>⋅⋅⋅⋅⋅⋅"viewCount":8<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|

**Тестовый набор - негативные проверки для параметра viewCount**

| Параметр | Описание |
| --- | --- |
| id | NEG_CREATE_ITEM_022 |
| Заголовок | Создание объявления невозможно, если передан недопустимый тип данных для параметра viewCount: str|
| Адрес сервера | https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса передать тип данных str в параметр viewCount, например: <br>{<br>⋅⋅⋅"sellerID":1234345989, <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"price":10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":5, <br>⋅⋅⋅⋅⋅⋅"likes":2, <br>⋅⋅⋅⋅⋅⋅"viewCount":"123"<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|

| Параметр | Описание |
| --- | --- |
| id | NEG_CREATE_ITEM_023 |
| Заголовок | Создание объявления невозможно, если передано очень большое значение int для параметра viewCount|
| Адрес сервера | https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса в параметр viewCount передать большое значение типа int, например: <br>{<br>⋅⋅⋅"sellerID":1234345989, <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"price":10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":5, <br>⋅⋅⋅⋅⋅⋅"likes":2, <br>⋅⋅⋅⋅⋅⋅"viewCount":400000000000000<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|

| Параметр | Описание |
| --- | --- |
| id | NEG_CREATE_ITEM_024 |
| Заголовок | Создание объявления невозможно, если передано логически некорректное значение для параметра viewCount - -1|
| Адрес сервера | https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить POST на возможность создания объявления - '/api/1/item', в теле запроса в параметр viewCount передать -1, например: <br>{<br>⋅⋅⋅"sellerID":1234345989, <br>⋅⋅⋅"name":"example", <br>⋅⋅⋅"price":10, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts":5, <br>⋅⋅⋅⋅⋅⋅"likes":2, <br>⋅⋅⋅⋅⋅⋅"viewCount":-1<br>⋅⋅⋅}<br>}|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|

#Тест-кейсы для ручки GET /api/1/item/{id} - получение объявления по его идентификатору

| Параметр | Описание |
| --- | --- |
| id | GET_ITEM_INFO_001 |
| Заголовок | Получение объявления по его id возможно, если передан корректный id существующего объявления|
| Адрес сервера | https://qa-internship.avito.com |
| Предусловие | Создать объявление (POST /api/1/item)|
| Шаги для воспроизведения | Отправить GET на возможность получения объявления по его id - '/api/1/item/{id}', в url параметр передать id существующего ранее созданного объявления, например: '5596170f-55c5-4411-82e2-e5acdee54854'|
| Ожидаемый результат | <br> 200 OK <br> Ошибок в структуре ответа нет: <br>[<br>{<br>⋅⋅⋅"ID": "string",<br>⋅⋅⋅"sellerID": int, <br>⋅⋅⋅"name": "string", <br>⋅⋅⋅"price": int, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts": int, <br>⋅⋅⋅⋅⋅⋅"likes": int, <br>⋅⋅⋅⋅⋅⋅"viewCount": int<br>⋅⋅⋅}<br>}<br>] <br> Параметры тела ответа совпадают с параметрами созданного объявления|

**Негативные проверки**

| Параметр | Описание |
| --- | --- |
| id | NEG_GET_ITEM_INFO_001 |
| Заголовок | Получение объявления по его id невозможно, если передан id несуществующего объявления|
| Адрес сервера | https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить GET на возможность получения объявления по его id - '/api/1/item/{id}', в url параметр передать id несуществующего объявления, например: 'ffffffff-ffff-ffff-ffff-ffffffffffff'|
| Ожидаемый результат | <br> 404 Not Found <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|

| Параметр | Описание |
| --- | --- |
| id | NEG_GET_ITEM_INFO_002 |
| Заголовок | Получение объявления по его id невозможно, если передан некорректный id - пробел|
| Адрес сервера | https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить GET на возможность получения объявления по его id - '/api/1/item/{id}', в url параметр передать пробел в качестве id, например: ' '|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|

| Параметр | Описание |
| --- | --- |
| id | NEG_GET_ITEM_INFO_003 |
| Заголовок | Получение объявления по его id невозможно, если передан некорректный id - отсутствуют "-"|
| Адрес сервера | https://qa-internship.avito.com |
| Предусловие | Создать объявление (POST /api/1/item)|
| Шаги для воспроизведения | Отправить GET на возможность получения объявления по его id - '/api/1/item/{id}', в url параметр передать id ранее созданного объявления без "-", например: '5596170f55c5441182e2e5acdee54854'|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|

#Тест-кейсы для ручки GET /api/1/statistic/{id} - получение статистики объявления по его идентификатору

| Параметр | Описание |
| --- | --- |
| id | GET_ITEM_STATISTICS_001 |
| Заголовок | Получение статистики объявления по его id возможно, если передан корректный id существующего объявления|
| Адрес сервера | https://qa-internship.avito.com |
| Предусловие | Создать объявление (POST /api/1/item) с заполненными параметрами параметра statistics|
| Шаги для воспроизведения | Отправить GET на возможность получения статистики объявления по его id - '/api/1/statistic/{id}', в url параметр передать id существующего ранее созданного объявления, например: '5596170f-55c5-4411-82e2-e5acdee54854'|
| Ожидаемый результат | <br> 200 OK <br> Ошибок в структуре ответа нет: <br>[<br>{<br>⋅⋅⋅"contacts": int, <br>⋅⋅⋅"likes": int, <br>⋅⋅⋅"viewCount": int<br>}<br>] <br> Параметры тела ответа совпадают с параметрами statistics ранее созданного объявления|

| Параметр | Описание |
| --- | --- |
| id | GET_ITEM_STATISTICS_002 |
| Заголовок | Получение статистики объявления по его id возможно, если передан корректный id существующего объявления, при создании которого параметр statistics не передавался|
| Адрес сервера | https://qa-internship.avito.com |
| Предусловие | Создать объявление (POST /api/1/item) с НЕ заполненными параметром statistics (не передавать)|
| Шаги для воспроизведения | Отправить GET на возможность получения статистики объявления по его id - '/api/1/statistic/{id}', в url параметр передать id существующего ранее созданного объявления, например: '5596170f-55c5-4411-82e2-e5acdee54854'|
| Ожидаемый результат | <br> 200 OK <br> Ошибок в структуре ответа нет: <br>[<br>{<br>⋅⋅⋅"contacts": 0, <br>⋅⋅⋅"likes": 0, <br>⋅⋅⋅"viewCount": 0<br>}<br>]|

**Негативные проверки**

| Параметр | Описание |
| --- | --- |
| id | NEG_GET_ITEM_STATISTICS_001 |
| Заголовок | Получение статистики объявления по его id невозможно, если передан id несуществующего объявления|
| Адрес сервера | https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить GET на возможность получения статистики объявления по его id - '/api/1/statistic/{id}', в url параметр передать id несуществующего объявления, например: 'ffffffff-ffff-ffff-ffff-ffffffffffff'|
| Ожидаемый результат | <br> 404 Not Found <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|

| Параметр | Описание |
| --- | --- |
| id | NEG_GET_ITEM_STATISTICS_002 |
| Заголовок | Получение статистики объявления по его id невозможно, если передан некорректный id - пробел|
| Адрес сервера | https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить GET на возможность получения статистики объявления по его id - '/api/1/statistic/{id}', в url параметр передать пробел в качестве id, например: ' '|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|

| Параметр | Описание |
| --- | --- |
| id | NEG_GET_ITEM_STATISTICS_003 |
| Заголовок | Получение статистики объявления по его id невозможно, если передан некорректный id - отсутствуют "-"|
| Адрес сервера | https://qa-internship.avito.com |
| Предусловие | Создать объявление (POST /api/1/item) с заполненными параметрами параметра statistics|
| Шаги для воспроизведения | Отправить GET на возможность получения статистики объявления по его id - '/api/1/statistic/{id}', в url параметр передать id ранее созданного объявления без "-", например: '5596170f55c5441182e2e5acdee54854'|
| Ожидаемый результат | <br> 400 Bad Request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}|

#Тест-кейсы для ручки GET /api/1/{sellerID}/item - получение всех объявлений по идентификатору продавца

| Параметр | Описание |
| --- | --- |
| id | GET_SELLER_ITEMS_001 |
| Заголовок | Получение всех объявлений продавца по его id возможно, если передан корректный id существующего продавца|
| Адрес сервера | https://qa-internship.avito.com |
| Предусловие | Создать объявление (POST /api/1/item), в котором sellerID = 1234345989 и заполнены параметры параметра statistics|
| Шаги для воспроизведения | Отправить GET на возможность получения всех объявлений продавца по его id - '/api/1/{sellerID}/item', в url параметр передать id существующего продавца, для которого ранее создали объявление, например: 1234345989|
| Ожидаемый результат | <br> 200 OK <br> Ошибок в структуре ответа нет:  <br>[<br>{<br>⋅⋅⋅"ID": "string", <br>⋅⋅⋅"sellerID": int, <br>⋅⋅⋅"name": "string", <br>⋅⋅⋅"price": int, <br>⋅⋅⋅"statistics": {<br>⋅⋅⋅⋅⋅⋅"contacts": int, <br>⋅⋅⋅⋅⋅⋅"likes": int, <br>⋅⋅⋅⋅⋅⋅"viewCount": int<br>⋅⋅⋅}<br>}<br>] <br> Параметры тела ответа совпадают с параметрами ранее созданного объявления|

| Параметр | Описание |
| --- | --- |
| id | GET_SELLER_ITEMS_002 |
| Заголовок | Запрос для получения всех объявлений продавца успешно обрабатывается, если передать id продавца, у которого нет объявлений|
| Адрес сервера | https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить GET на возможность получения всех объявлений продавца по его id - '/api/1/{sellerID}/item', в url параметр передать id существующего продавца, у которого нет объявлений, например: 1234345977|
| Ожидаемый результат | <br> 200 OK <br> Ошибок в структуре ответа нет: <br>[] 

**Негативные проверки**

| Параметр | Описание |
| --- | --- |
| id | NEG_GET_SELLER_ITEMS_001 |
| Заголовок | Запрос для получения всех объявлений продавца не обрабатывается, если передать некорректный id - 0|
| Адрес сервера | https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить GET на возможность получения всех объявлений продавца по его id - '/api/1/{sellerID}/item', в url параметр передать id = 0|
| Ожидаемый результат | <br> 400 Bad request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}

| Параметр | Описание |
| --- | --- |
| id | NEG_GET_SELLER_ITEMS_002 |
| Заголовок | Запрос для получения всех объявлений продавца не обрабатывается, если передать некорректный id - пробел|
| Адрес сервера | https://qa-internship.avito.com |
| Шаги для воспроизведения | Отправить GET на возможность получения всех объявлений продавца по его id - '/api/1/{sellerID}/item', в url параметр передать пробел в качестве id|
| Ожидаемый результат | <br> 400 Bad request <br> Ошибок в структуре ответа нет: <br>{<br>⋅⋅⋅"result": {<br>⋅⋅⋅⋅⋅⋅"message": "string",<br>⋅⋅⋅⋅⋅⋅"messages": {<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp1": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp2": "string",<br>⋅⋅⋅⋅⋅⋅⋅⋅⋅"additionalProp3": "string"<br>⋅⋅⋅⋅⋅⋅⋅}<br>⋅⋅⋅},<br>⋅⋅⋅"status": "string"<br>}
