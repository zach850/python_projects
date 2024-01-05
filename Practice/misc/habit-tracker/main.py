# https://pixe.la/
# https://docs.pixe.la/entry/post-pixel

import requests
from datetime import datetime

USERNAME = "zrichter"
TOKEN = "24hfow90ruf2g"
GRAPH_ID = "graph1"

pixela_endpoint = " https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

headers = {"X-USER-Token": TOKEN}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# graph_config = {
#     "id": "graph1",
#     "name": "Running Graph",
#     "unit": "Miles",
#     "type": "float",
#     "color": "sora",

# }

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
print(today.strftime("%Y%m%d"))

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many miles did you run today? "),
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)
