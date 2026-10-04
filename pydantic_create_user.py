from pydantic import BaseModel, EmailStr


class ShortUserDataSchema(BaseModel):
    """Вспомогательная модель с данными пользователя."""
    email: EmailStr
    lastName: str
    firstName: str
    middleName: str


class UserSchema(ShortUserDataSchema):
    """Информация о пользователе."""
    id: str


class CreateUserRequestSchema(ShortUserDataSchema):
    """Данные запроса на создание пользователя."""
    password: str


class CreateUserResponseSchema(BaseModel):
    """Данные успешного ответа на запрос о создании пользователя."""
    user: UserSchema
