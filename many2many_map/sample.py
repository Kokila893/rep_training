import json
import requests
from requests import Response


def send_data(url, data):
    response = requests.post(url, json=data)
    return response


# send_data('http://localhost:8000/users/',{'username':'xxx'})
# send_data('http://localhost:8000/cars/', {'model':'aaa'})
# send_data('http://localhost:8000/cars/', json.dumps({
#         "model": "modela"
# }))
#
# send_data('http://localhost:8000/LinkCartoUser/', {
#     'Car': 3,
#     'User': [3,4,5]
# })

send_data('http://localhost:8000/LinkUsertoCar/', {
    'User': 4,
    'Car': [3, 5]
})



























# send_data('http://localhost:8000/LinkUsertoCar/',json.dumps(LinkCartoUser={
#         'Car':1,
#         'User':(1,2,3,4,5)
#         }))
# linkUsertoCar= {
#      'User': 1,
#      'Car': [1,2,3,4,5]
#  }
# req = linkUsertoCar


# url='http://localhost:8000/users/'
# data=json.dumps(
#     {'username': 'xxx' }
# )
# headers = {
#     'Content-Type': 'application/json'
# }


# res=requests.post('http://localhost:8000/users/',data=json.dumps({'username': 'xxx' }),
#                       headers={'Content-Type': 'application/json'})
# print(res)
#
# req=requests.put('http://localhost:8000/notes/2',data=json.dumps({'username':'aaa'}),
#              headers={'Content-Type': 'application/json'})
#
#
# print(req)


# Response1 = requests.post('http://localhost:8000/cars/',
#              headers={'Content-Type': 'application/json'},
#              data=json.dumps({'model': 'i20' }))


# abc=requests.put('http://localhost:8000/users/5',
#                 headers={'Content-Type': 'application/json'},
#                 data=json.dumps({'username':'aaa'}))
# print(abc)
# nested-resources added
# val=[]
# response=requests.post('http://localhost:8000/notes/',
#               headers={'Content-Type': 'application/json'},
#               data=json.dumps({"title": "abc222",
#                                "description": "zzzzzzzz",
#                                "created_at": "AP",
#                                "created_by": "abc",
#                                "priority": 2,
#                                "books": [
#                                    {
#                                         "name": "zzz"
#                                    }
#                                ]
#                                }))
# val.append(response)
# print(val)


# val=[]
# response=requests.post('http://localhost:8000/notes/',
#               headers={'Content-Type': 'application/json'},
#               data=json.dumps({"title": "abc222",
#                                "description": "zzzzzzzz",
#                                "created_at": "AP",
#                                "created_by": "abc",
#                                "priority": 2,
#                                "books": [
#                                    {
#                                         "name": "zzz"
#                                    }
#                                ]
#                                }))
# val.append(response)
# print(val)
#
# # cat post.json | http POST http://localhost:8000/notes
# valput=[]
# abc=requests.put('http://localhost:8000/notes/1',
#                 headers={'Content-Type': 'application/json'},
#                 data=json.dumps({"title": "abc123",
#                                "description": "xxxxxxxxx",
#                                "created_at": "TN",
#                                "created_by": "def",
#                                "priority": 1,
#                                "books": [
#                                    {
#                                         "name": "xyz"
#                                    }
#                                ]
#                                }))
# valput.append(abc)
# print(valput)
