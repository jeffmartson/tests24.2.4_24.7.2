import requests

# Задаем auth_key
auth_key = "8fd8078ecf1741710b7f1fd1be4eeadc469203dc89599de6be5bc6df"

# Тест-кейс 1: Позитивный тест добавления нового питомца без фотографии
def test_add_pet_without_photo():
    data = {
        "name": "Catty",
        "animal_type": "Cat",
        "age": 2
    }

    response = requests.post("https://petfriends.skillfactory.ru/api/create_pet_simple", headers={"auth_key": auth_key}, data=data)

    assert response.status_code == 200
    assert "id" in response.json()

# Тест-кейс 2: Позитивный тест добавления нового питомца с фотографией
def test_add_pet_with_photo():
    data = {
        "name": "Catty",
        "animal_type": "Cat",
        "age": 2
    }

    files = {"pet_photo": ("photo.jpg", open("photo.jpg", "rb"))}

    response = requests.post("https://petfriends.skillfactory.ru/api/pets", headers={"auth_key": auth_key}, data=data, files=files)

    assert response.status_code == 200
    assert "id" in response.json()

# Тест-кейс 3: Негативный тест добавления нового питомца без auth_key
def test_add_pet_without_auth_key():
    data = {
        "name": "Catty",
        "animal_type": "Cat",
        "age": 2
    }

    response = requests.post("https://petfriends.skillfactory.ru/api/create_pet_simple", data=data)

    assert response.status_code == 403

# Тест-кейс 4: Негативный тест добавления нового питомца с неверными данными (без имени)
def test_add_pet_without_name():
    data = {
        "animal_type": "Cat",
        "age": 2
    }

    response = requests.post("https://petfriends.skillfactory.ru/api/create_pet_simple", headers={"auth_key": auth_key}, data=data)

    assert response.status_code == 400

# Тест-кейс 5: Позитивный тест получения API ключа
def test_get_api_key():
    email = "jeffmartson@gmail.com"
    password = "n!9FrP$JiMTpwv$kjzyg&if5qh"

    response = requests.get("https://petfriends.skillfactory.ru/api/key", headers={"email": email, "password": password})

    assert response.status_code == 200
    assert "key" in response.json()

# Тест-кейс 6: Позитивный тест получения списка питомцев с auth_key
def test_get_pets_list():
    response = requests.get("https://petfriends.skillfactory.ru/api/pets", headers={"auth_key": auth_key})

    assert response.status_code == 200
    assert "pets" in response.json()

# Тест-кейс 7: Негативный тест добавления фотографии питомца без auth_key
def test_add_pet_photo_without_auth_key():
    pet_id = "ID_питомца"

    with open("файл_с_фотографией.jpg", "rb") as file:
        response = requests.post(f"https://petfriends.skillfactory.ru/api/pets/set_photo/{pet_id}", files={"pet_photo": file})

    assert response.status_code == 403  # Должно быть 403, так как auth_key отсутствует

# Тест-кейс 8: Позитивный тест удаления информации о питомце
def test_delete_pet_info():
    pet_id = "ID_питомца_для_удаления"

    response = requests.delete(f"https://petfriends.skillfactory.ru/api/pets/{pet_id}", headers={"auth_key": auth_key})

    assert response.status_code == 200  # Питомец должен быть успешно удален

# Тест-кейс 9: Негативный тест обновления информации о питомце с неверным auth_key
def test_update_pet_info_with_invalid_auth_key():
    pet_id = "ID_питомца_для_обновления"
    data = {
        "name": "Новое_имя",
        "animal_type": "Новый_вид",
        "age": 3
    }

    response = requests.put(f"https://petfriends.skillfactory.ru/api/pets/{pet_id}", headers={"auth_key": "неверный_auth_key"}, data=data)

    assert response.status_code == 403  # Должно быть 403, так как auth_key неверен

# Тест-кейс 10: Позитивный тест обновления информации о питомце с правильными данными
def test_update_pet_info():
    pet_id = "ID_питомца_для_обновления"
    data = {
        "name": "Новое_имя",
        "animal_type": "Новый_вид",
        "age": 3
    }

    response = requests.put(f"https://petfriends.skillfactory.ru/api/pets/{pet_id}", headers={"auth_key": auth_key}, data=data)

    assert response.status_code == 200  # Информация о питомце должна быть успешно обновлена

# Тест-кейс 11: Позитивный тест добавления питомца с фотографией
def test_add_pet_with_photo():
    data = {
        "name": "Питомец_с_фото",
        "animal_type": "Собака",
        "age": 2
    }

    with open("файл_с_фотографией.jpg", "rb") as file:
        response = requests.post("https://petfriends.skillfactory.ru/api/pets", headers={"auth_key": auth_key}, data=data, files={"pet_photo": file})

    assert response.status_code == 200  # Должно быть 200, питомец с фотографией успешно добавлен
    assert "pet_id" in response.json()

# Тест-кейс 12: Негативный тест добавления питомца без имени
def test_add_pet_without_name():
    data = {
        "animal_type": "Собака",
        "age": 2
    }

    response = requests.post("https://petfriends.skillfactory.ru/api/pets", headers={"auth_key": auth_key}, data=data)

    assert response.status_code == 400  # Должно быть 400, так как имя питомца обязательное поле

# Тест-кейс 13: Негативный тест обновления информации о питомце с неверным pet_id
def test_update_pet_info_with_invalid_pet_id():
    pet_id = "несуществующий_питомец"
    data = {
        "name": "Новое_имя",
        "animal_type": "Новый_вид",
        "age": 3
    }

    response = requests.put(f"https://petfriends.skillfactory.ru/api/pets/{pet_id}", headers={"auth_key": auth_key}, data=data)

    assert response.status_code == 400  # Должно быть 400, так как pet_id не существует

# Тест-кейс 14: Негативный тест удаления информации о питомце с неверным pet_id
def test_delete_pet_info_with_invalid_pet_id():
    pet_id = "несуществующий_питомец"

    response = requests.delete(f"https://petfriends.skillfactory.ru/api/pets/{pet_id}", headers={"auth_key": auth_key})

    assert response.status_code == 400  # Должно быть 400, так как pet_id не существует

# Тест-кейс 15: Негативный тест обновления информации о питомце без auth_key
def test_update_pet_info_without_auth_key():
    pet_id = "ID_питомца_для_обновления"
    data = {
        "name": "Новое_имя",
        "animal_type": "Новый_вид",
        "age": 3
    }

    response = requests.put(f"https://petfriends.skillfactory.ru/api/pets/{pet_id}", data=data)

    assert response.status_code == 403  # Должно быть 403, так как auth_key отсутствует

# Тест-кейс 16: Негативный тест удаления информации о питомце без auth_key
def test_delete_pet_info_without_auth_key():
    pet_id = "ID_питомца_для_удаления"

    response = requests.delete(f"https://petfriends.skillfactory.ru/api/pets/{pet_id}")

    assert response.status_code == 403  # Должно быть 403, так как auth_key отсутствует

# Запуск всех тестов
if __name__ == "__main__":
    test_add_pet_without_photo()
    test_add_pet_with_photo()
    test_add_pet_without_auth_key()
    test_add_pet_without_name()
    test_get_api_key()
    test_get_pets_list()
    test_add_pet_photo_without_auth_key()
    test_delete_pet_info()
    test_update_pet_info_with_invalid_auth_key()
    test_update_pet_info()
    test_update_pet_info_with_invalid_pet_id()
    test_delete_pet_info_with_invalid_pet_id()
    test_update_pet_info_without_auth_key()
    test_delete_pet_info_without_auth_key()




