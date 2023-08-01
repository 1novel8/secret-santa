from src.apps.core.repositories import BaseRepository

from .models import Present


class PresentRepository(BaseRepository):
    model = Present
