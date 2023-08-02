from .repositories import PartyRepository
from apps.core.services import BaseService


class PartyService(BaseService):
    repository = PartyRepository()
