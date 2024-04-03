import requests
import pytest
import allure

@allure.feature("Тестирование API пользователей")
@allure.epic("API Тестирование")
class TestApi:
    @allure.story("Получение данных одного пользователя")
    def test_single_user(self):
        url = "https://reqres.in/api/users/2"
        with allure.step("Отправка GET запроса для получения данных пользователя"):
            response = requests.get(url)
        assert response.status_code == 200
        
        with allure.step("Проверка заголовка Content-Type"):
            assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
        
        user_data = response.json()["data"]
        with allure.step("Проверка атрибутов данных пользователя"):
            assert "id" in user_data
            assert "email" in user_data
            assert "first_name" in user_data
            assert "last_name" in user_data
            assert "avatar" in user_data

    @allure.story("Создание пользователя")
    def test_create_user(self):
        url = "https://reqres.in/api/users"
        data = {
            "name": "morpheus",
            "job": "leader"
        }
        with allure.step("Отправка POST запроса для создания нового пользователя"):
            response = requests.post(url, json=data)
        assert response.status_code == 201
        
        with allure.step("Проверка заголовка Content-Type"):
            assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
        
        user_data = response.json()
        with allure.step("Проверка атрибутов данных пользователя"):
            assert "id" in user_data
            assert "name" in user_data
            assert "job" in user_data
            assert "createdAt" in user_data

    @allure.story("Обновление данных пользователя")
    def test_update_user(self):
        url = "https://reqres.in/api/users/2"
        data = {
            "name": "morpheus",
            "job": "zion resident"
        }
        with allure.step("Отправка PUT запроса для обновления данных пользователя"):
            response = requests.put(url, json=data)
        assert response.status_code == 200
        
        with allure.step("Проверка заголовка Content-Type"):
            assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
        
        user_data = response.json()
        with allure.step("Проверка обновленных атрибутов данных пользователя"):
            assert "name" in user_data
            assert "job" in user_data
            assert "updatedAt" in user_data

    @allure.story("Удаление пользователя")
    def test_delete_user(self):
        url = "https://reqres.in/api/users/2"
        with allure.step("Отправка DELETE запроса для удаления пользователя"):
            response = requests.delete(url)
        assert response.status_code == 204