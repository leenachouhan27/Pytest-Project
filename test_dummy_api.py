from http.client import responses

import requests
#import  json

url = "https://reqres.in/"

def test_get_data():
    endpoint = "/api/users?page=2"
    response = requests.get(url+endpoint)
    assert response.status_code == 200
    data = response.json()
    assert data["data"][0]["first_name"] == "Michael"

def test_get_single_user():
    endpoint = "/api/users/587"
    response = requests.get(url+endpoint)
    assert response.status_code == 200
    print(response.json())

def test_single_user_not_found():
    endpoint = "/api/users/923"
    response = requests.get(url+endpoint)
    assert response.status_code == 404

def test_create_user():
    endpoint = "/api/users"
    json = {
    "name": "morpheus",
    "job": "leader"
}
    response = requests.post(url+endpoint,json=json)
    assert  response.status_code == 201
    data = response.json()['id']
    print(data)

def test_update_user():
    json = {
    "name": "morpheus",
    "job": "zion resident"
}
    endpoint = "/api/users/2"
    response = requests.put(url+endpoint)
    print(response.status_code)

