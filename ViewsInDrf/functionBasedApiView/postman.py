import requests
import json

URL = "http://127.0.0.1:8000/students/"
PRIMARYKYEURL = "http://127.0.0.1:8000/students/{}"

def get_data():
    data = {}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)

def save_data():
    data = {"id":99, "name": "suhail", "score":75.2 }
    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    r = requests.post(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)

def get_data_by_Id(id):
    data = {}
    json_data = json.dumps(data)
    r = requests.get(url=PRIMARYKYEURL.format(id), data=json_data)
    data = r.json()
    print(data)

def update_data(id):
    data = {"id":2258, "name": "yadav", "score":75.0 }
    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    r = requests.put(url=PRIMARYKYEURL.format(id), headers=headers, data=json_data)
    data = r.json()
    print(data)

save_data()
# get_data()
#get_data_by_Id(2)
# update_data(2)


