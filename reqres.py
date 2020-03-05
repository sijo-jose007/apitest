import requests
from requests.exceptions import HTTPError

from apilist import api_list


# get request
def get_request(url):
    response = requests.get(url)
    try:
        assert response.status_code == 200
        print(response.content)
        print(response.headers)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')


# post request
def post_request(url, postdata):
    response = requests.post(url, data=postdata)
    try:
        assert response.status_code == 201
        json_response = response.json()
        print(f"json response {json_response}")
    except Exception as err:
        print(f'Other error occurred: {err}')


# put request
def put_request(url, putdata):
    response = requests.post(url, data=putdata)
    print(f"put status code: {response.status_code}")
    try:
        assert response.status_code == 201
        json_response = response.json()
        print(f"json response {json_response}")
    except Exception as err:
        print(f'Other error occurred: {err}')


# patch request
def patch_request(url, patchdata):
    response = requests.post(url, data=patchdata)
    print(f"put status code: {response.status_code}")
    try:
        assert response.status_code == 201
        json_response = response.json()
        print(f"json response {json_response}")
    except Exception as err:
        print(f'Other error occurred: {err}')


get_request(api_list.list_users)

data = {
    "name": "morpheus",
    "job": "leader"
}
# post_request(api_list.create_user, data)
put_data = {
    "name": "morpheus",
    "job": "zion resident"
}

# put_request(api_list.update_put, put_data)

patch_data = {
    "job": "Developer"
}

patch_request(api_list.update_patch, patch_data)

