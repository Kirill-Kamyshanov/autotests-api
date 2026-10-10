import httpx

from tools.fakers import fake

host = "http://127.0.0.1:8000"

create_user_payload = {
    "email": get_random_email(),
    "password": "qwerty",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = httpx.post(f'{host}/api/v1/users', json=create_user_payload)
print(create_user_response.status_code)
created_user_data = create_user_response.json()
user_id = created_user_data['user']['id']

login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}
login_response = httpx.post(f'{host}/api/v1/authentication/login', json=login_payload)
print(login_response.status_code)
access_token = login_response.json()['token']['accessToken']

update_payload = {
    "email": get_random_email(),
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
update_response = httpx.patch(f'{host}/api/v1/users/{user_id}',
                              headers={"Authorization": f"Bearer {access_token}"},
                              json=update_payload)
print(update_response.status_code)
print(update_response.json())
