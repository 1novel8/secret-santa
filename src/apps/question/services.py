from apps.core.services import BaseService
from .repositories import QuestionRepository


class QuestionService(BaseService):
    repository = QuestionRepository()
