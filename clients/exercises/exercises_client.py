from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class GetExercisesApiRequest(TypedDict):
    courseId: str


class CreateExerciseApiRequest(TypedDict):
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExerciseApiRequest(TypedDict):
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(APIClient):
    """Клиент для работы с /api/v1/exercises"""

    def get_exercises_api(self, query: GetExercisesApiRequest) -> Response:
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

    def create_exercise_api(self, request: CreateExerciseApiRequest) -> Response:
        """
        Создание задания.

        :param request: Словарь с данными для тела запроса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseApiRequest) -> Response:
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
