from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, permissions, status

from .models import Party
from .serializers import BasePartySerializer, InviteUserSerializer
from .services import PartyService
from apps.core import mixins as custom_mixins
from .tasks import invite_user_by_email, remind_users
from apps.authentication.services import UserService


@extend_schema(tags=['party'])
class PartyViewSet(custom_mixins.SerializeByActionMixin,
                   mixins.ListModelMixin,
                   custom_mixins.UpdateModelMixin,
                   custom_mixins.RetrieveModelMixin,
                   custom_mixins.CreateModelMixin,
                   custom_mixins.DestroyModelMixin,
                   GenericViewSet):
    queryset = Party.objects.all()
    serializer_class = BasePartySerializer
    service = PartyService()
    serialize_by_action = {
        'retrieve': BasePartySerializer,
        'create': BasePartySerializer,
        'partial_update': BasePartySerializer,
        'destroy': BasePartySerializer,
        'invite': InviteUserSerializer,
        'join': None,
    }

    permission_classes = (permissions.IsAuthenticated,)

    http_method_names = ['get', 'patch', 'put', 'post', 'delete']

    def list(self, request, *args, **kwargs):
        queryset = self.service.list(user=self.request.user, **kwargs)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, **kwargs):
        return self.service.create(user=self.request.user, **kwargs)

    def perform_update(self, **kwargs):
        return self.service.update(user=self.request.user, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        obj = self.service.get_by_id(user=self.request.user, **kwargs)
        serializer = self.get_serializer(instance=obj)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        self.service.delete(user=self.request.user, **kwargs)

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=["POST"], detail=True, url_path='invite')
    def invite(self, request, **kwargs):
        user_service = UserService()
        party = self.service.get_by_id(user=self.request.user, **kwargs)

        if user_service.is_email_exist(**request.data):
            user = user_service.get_by_email(**request.data)
        else:
            user = user_service.create(**request.data)

        self.service.invite_user(
            inviter=self.request.user,
            user=user,
            party=self.service.get_by_id(user=self.request.user, **kwargs),
        )
        invite_user_by_email.delay(
            party_id=party.id,
            party_name=party.name,
            **request.data
        )

        return Response(status=status.HTTP_200_OK)

    @action(methods=["POST"], detail=True, url_path='join')
    def join(self, request, **kwargs):
        self.service.confirm_user(
            user=self.request.user,
            **kwargs,
        )
        return Response(status=status.HTTP_200_OK)

    @action(methods=["GET"], detail=False)
    def test(self, request):
        remind_users.delay()
        return Response(status=status.HTTP_200_OK)
