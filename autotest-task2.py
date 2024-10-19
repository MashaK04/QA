import requests
import pytest
import random

BASE_URL = "https://qa-internship.avito.com/api/1"

# Генерация уникального sellerId
def un_seller_id():
    return random.randint(111111, 999999)

#Проверка получения объявления
def test_get_info_item():
    item_id = "7a8fe969-2a57-468e-82c9-1982d22023c5"
    url = f"{BASE_URL}/item/{item_id}"
    response = requests.get(url)

    # Проверка метода запроса
    assert response.request.method == 'GET', "Метод запроса должен быть GET"

    # Проверка статуса ответа
    assert response.status_code == 200, "Ожидаемый статус 200"
    json_data = response.json()

    # Проверка, что ответ является словарем
    assert isinstance(json_data, list), "Ответ должен быть в виде списка"



#Получение всех объявлений по продавцам
def test_get_items_by_seller():
    seller_id = un_seller_id()
    url = f"{BASE_URL}/{seller_id}/item"
    response = requests.get(url)

    # Проверка метода запроса
    assert response.request.method == 'GET', "Метод запроса должен быть GET"

    # Проверка статуса ответа
    assert response.status_code == 200, "Ожидаемый статус кода 200"

    json_data = response.json()

    # Проверка, что ответ является списком
    assert isinstance(json_data, list), "Ответ должен быть в виде списка"



#Сохранение объявления
def test_post_item():
    url = f"{BASE_URL}/item"
    payload = {
        "name": "Телефон",
        "price": 85566,
        "sellerId": 3452,
        "statistics": {
            "contacts": 32,
            "like": 35,
            "viewCount": 14
        }
    }

    response = requests.post(url, json=payload)

    # Проверка метода запроса
    assert response.request.method == 'POST', "Метод запроса должен быть POST"

    #Проверка статуса ответа
    assert response.status_code == 201, "Ожидаемый ответ со статусом 201 - создание"

    json_data = response.json()

    # Проверка, что результат в виде списка
    assert isinstance(json_data, list), "Ответ в виде списка"

if __name__ == "__main__":
    pytest.main()
