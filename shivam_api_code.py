import json
from random import random
import requests

url="https://example.com"
path="/service/Virtual-Machine"

name = random()
body={
    "name": "Vm_name",
    "quantity": 2
}

contents= {
    "Accept": "application/json"
}

response = requests.post(url+path, json=body, headers=contents)

assert response.status_code == 200

print(response.json())
response_body = json.loads(response.text)
assert response_body["VM_Price"] == 121


path2="/ordered-services/VM"
param= {"name": "VM_name", "location": "eastus"}
response2 = requests.get(url+path2, params=param)
assert response2.status_code == 200
for i in response2.json():
    print(i['name'], i['price'])