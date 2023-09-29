from django.db.models import F

from apps.core.repositories import BaseRepository

from apps.present.models import Present
from apps.authentication.models import User


class PresentRepository(BaseRepository):
    model = Present

    def add_user(self, user: User, present: Present, is_preferred: bool) -> Present:
        present.users.add(
            user,
            through_defaults={'is_preferred': is_preferred}
        )
        return present

    def list(self, **kwargs):
        present_list = self.model.objects.all()
        return present_list

    def user_list(self, **kwargs):
        present_list = (self.model.objects.filter(userpresent__user_id=kwargs.get('user_id'))
                        .prefetch_related('userpresent').values('id',
                                                                'name',
                                                                'description',
                                                                'image',
                                                                'url',
                                                                is_preferred=F('userpresent__is_preferred')))
        return present_list
