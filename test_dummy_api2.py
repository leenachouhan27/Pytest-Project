import requests
import pytest

base_url = "http://216.10.245.166/"
data = ""

@pytest.mark.p1
def test_get_book_by_auther():
    endpoint = "/Library/GetBook.php?AuthorName=leena"
    response = requests.get(base_url+endpoint)
    assert response.status_code == 200
    assert response.json()[0]['book_name'] == "Appium Automation with python"

@pytest.mark.p1
def test_add_book():
    endpoint = "Library/Addbook.php"
    json = {

"name":"ye book mene likhi he",
"isbn":"Namdev",
"aisle":"857894",
"author":"The great leena"
}

    response = requests.post(base_url+endpoint,json=json)
    assert response.status_code == 200
    assert  response.json()["Msg"] == "successfully added"
    global data
    data = response.json()["ID"]
    print(data)

@pytest.mark.p2
def test_book_by_id():
    endpoint = "Library/GetBook.php?ID="+data
    response = requests.get(base_url+endpoint)
    print(response.json())

@pytest.mark.p1
@pytest.mark.skipif(test_add_book(),reason="No need to run if book not added")
def test_delete_book_by_id():
    endpoint = "Library/DeleteBook.php"
    json = {"ID" : data}
    response = requests.post(base_url+endpoint,json = json)
    assert response.json()["msg"] == "book is successfully deleted"