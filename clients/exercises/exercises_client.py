from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema


class Exercise(TypedDict):
    """Описание структуры задания."""
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExercisesResponseDict(TypedDict):
    """Описание структуры ответа получения списка заданий."""
    exercises: list[Exercise]


class GetExerciseResponseDict(TypedDict):
    """Описание структуры ответа получения информации о задании."""
    exercise: Exercise


class CreateExerciseResponseDict(TypedDict):
    """Описание структуры ответа создания задания."""
    exercise: Exercise


class UpdateExerciseResponseDict(TypedDict):
    """Описание структуры ответа обновления задания."""
    exercise: Exercise


class GetExercisesQueryDict(TypedDict):
    """Описание параметров запроса для получения данных о курсах."""
    courseId: str


class CreateExerciseRequestDict(TypedDict):
    """Описание структуры запроса создания задания."""
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExerciseRequestDict(TypedDict):
    """Описание структуры запроса обновления задания."""
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(APIClient):
    """Клиент для работы с /api/v1/exercises"""

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Получение списка заданий для определенного курса.

        :param query: Словарь с courseId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Получение информации о задании по exercise_id.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Создание задания.

        :param request: Словарь с данными для тела запроса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Обновление данных задания.

        :param exercise_id: Идентификатор задания.
        :param request: Словарь с данными для тела запроса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Удаление задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        """
        Получение информации о задании и возврат ответа в формате json.

        :param exercise_id: Идентификатор задания.
        :return: Тело ответа - объект GetExerciseResponseDict.
        """
        response = self.get_exercise_api(exercise_id=exercise_id)
        return response.json()

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        """
        Получение списка заданий для определённого курса и возврат ответа в формате json.

        :param query: Словарь с courseId
        :return: Тело ответа - объект GetExercisesResponseDict.
        """
        response = self.get_exercises_api(query=query)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        """
        Создание задания и возврат ответа в формате json.

        :param request: Словарь с данными для тела запроса
        :return: Тело ответа - объект CreateExerciseResponseDict.
        """
        response = self.create_exercise_api(request=request)
        return response.json()

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> UpdateExerciseResponseDict:
        """
        Обновление данных задания и возврат ответа в формате json.

        :param exercise_id: Идентификатор задания
        :param request: Словарь с данными для тела запроса
        :return: Тело ответа - объект CreateExerciseResponseDict.
        """
        response = self.update_exercise_api(request=request, exercise_id=exercise_id)
        return response.json()


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
