from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client, CreateUserRequestSchema
from clients.users.users_schema import GetUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import get_random_email

create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)
# Инициализация публичного клиента
public_users_client = get_public_users_client()

# Создание пользователя
create_user_response = public_users_client.create_user(create_user_request)

# Инициализация приватного клиента
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
private_users_client = get_private_users_client(authentication_user)

# Получение данных пользователя
get_user_response = private_users_client.get_user_api(create_user_response.user.id)

# Генерация json-схемы
get_user_response_schema = GetUserResponseSchema.model_json_schema()

# Валидация JSON схемы ответа
validate_json_schema(instance=get_user_response.json(), schema=get_user_response_schema)
