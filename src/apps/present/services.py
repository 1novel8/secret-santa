from src.apps.core.services import BaseService
from .repositories import PresentRepository


class PresentService(BaseService):
    repository = PresentRepository()
