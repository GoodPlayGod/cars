import requests

base_url = 'http://localhost:8000'
add_car_url = f'{base_url}/add_car'
get_cars_url = f'{base_url}/cars'
get_car_by_id_url = f'{base_url}/get_car_by_id'
delete_car_url = f'{base_url}/delete_car'

new_car = {
    "id": 99,
    "make": "Toyota",
    "model": "Camry",
    "year": 2020,
    "price_per_day": 45.99
}


def test_health_check():
    response = requests.get(f"{base_url}/health")
    assert response.status_code == 200
    assert response.json() == {"message": "Service alive"}


def test_add_car():
    response = requests.post(add_car_url, json=new_car)
    assert response.status_code == 200
    assert response.json()['make'] == new_car['make']


def test_get_cars():
    response = requests.get(get_cars_url)
    assert new_car in response


def test_get_car_by_id():
    response = requests.get(f"{get_car_by_id_url}/99")
    assert response.status_code == 200
    assert response.json()['make'] == new_car['make']


def test_delete_car():
    delete_response = requests.delete(f"{delete_car_url}/99")
    assert delete_response.status_code == 200
    response = requests.get(f"{get_car_by_id_url}/1")
    assert response.status_code == 404
