import allure
from httpx import Response

from clients.api_client import APIClient
from clients.exercises.exercises_schema import GetExercisesQuerySchema, UpdateExerciseResponseSchema, \
    UpdateExerciseRequestSchema, CreateExerciseRequestSchema, CreateExerciseResponseSchema, GetExercisesResponseSchema, \
    GetExerciseResponseSchema
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from tools.routes import APIRoutes


class ExercisesClient(APIClient):
    """Клиент для работы с /api/v1/exercises"""

    @allure.step("Get exercises")
    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Получение списка заданий для определенного курса.

        :param query: Словарь с courseId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(APIRoutes.EXERCISES, params=query.model_dump(by_alias=True))

    @allure.step("Get exercise by id {exercise_id}")
    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Получение информации о задании по exercise_id.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"{APIRoutes.EXERCISES}/{exercise_id}")

    @allure.step("Create exercise")
    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Создание задания.

        :param request: Словарь с данными для тела запроса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(APIRoutes.EXERCISES, json=request.model_dump(by_alias=True))

    @allure.step("Update exercise by id {exercise_id}")
    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Обновление данных задания.

        :param exercise_id: Идентификатор задания.
        :param request: Словарь с данными для тела запроса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"{APIRoutes.EXERCISES}/{exercise_id}", json=request.model_dump(by_alias=True))

    @allure.step("Delete exercise by id {exercise_id}")
    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Удаление задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"{APIRoutes.EXERCISES}/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        """
        Получение информации о задании и возврат ответа в формате json.

        :param exercise_id: Идентификатор задания.
        :return: Тело ответа - объект GetExerciseResponseSchema.
        """
        response = self.get_exercise_api(exercise_id=exercise_id)
        return GetExerciseResponseSchema.model_validate(response.text)

    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        """
        Получение списка заданий для определённого курса и возврат ответа в формате json.

        :param query: Словарь с courseId
        :return: Тело ответа - объект GetExercisesResponseSchema.
        """
        response = self.get_exercises_api(query=query)
        return GetExercisesResponseSchema.model_validate(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        """
        Создание задания и возврат ответа в формате json.

        :param request: Словарь с данными для тела запроса
        :return: Тело ответа - объект CreateExerciseResponseSchema.
        """
        response = self.create_exercise_api(request=request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> UpdateExerciseResponseSchema:
        """
        Обновление данных задания и возврат ответа в формате json.

        :param exercise_id: Идентификатор задания
        :param request: Словарь с данными для тела запроса
        :return: Тело ответа - объект CreateExerciseResponseSchema.
        """
        response = self.update_exercise_api(request=request.model_dump(by_alias=True), exercise_id=exercise_id)
        return UpdateExerciseResponseSchema.model_validate(response.text)


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
