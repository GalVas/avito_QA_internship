**Протестировано на Python 3.7**
- Для запуска тестов должны быть установлены пакеты pytest, requests, copy, jsonschema
- Запуск всех тестов выполянется командой pytest


- **case 1** - папка 1 задания
  - **images** - папка со скриншотами багов
  - **BUGS_FROM_SCREENSHOT.md** - файл с описанием найденных багов
  
- **case 2.1** - папка 2.1 задания
  - **tests_create_item.py** - автотесты для запуска проверок для endpoint POST /api/1/item
  - **tests_get_item_info.py** - автотесты для запуска проверок для endpoint GET /api/1/item/{id}
  - **tests_get_item_statistics.py** - автотесты для запуска проверок для endpoint GET /api/1/statistic/{id}
  - **tests_get_seller_items.py** - автотесты для запуска проверок для endpoint GET /api/1/{sellerID}/item}
  - **test_cases.py** - тестовые данные
  - **BUGS.md** - файл с описанием найденных багов (баг-репорты)
  - **TESTCASES.md** - файл с описанием тест-кейсов для проведения проверок
  - **data.py** - исходные данные для тестов
  - **utils.py** - вспомогательные функции
  - **configuration.py** - endpoint-ы
  