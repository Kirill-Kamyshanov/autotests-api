import httpx

host = 'http://localhost:8000'

payload = {
    "email": "nestor10000@mail.ru",
    "password": "qwerty"
}
login_response = httpx.post(f"{host}/api/v1/authentication/login", json=payload)
access_token = login_response.json()['token']['accessToken']

get_user_response = httpx.get(f"{host}/api/v1/users/me", headers={"Authorization": f"Bearer {access_token}"})
print("Статус-код:", get_user_response.status_code)
print("Данные пользователя:", get_user_response.json())
