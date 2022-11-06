from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from project_time_tracking.api.models.user import User
from project_time_tracking.api.permissions import IsOwner
from project_time_tracking.api.serializers.user import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        if self.action == 'list':
            permission_classes = [IsAdminUser]
        if self.action in ['retrieve', 'partial_update', 'update']:
            permission_classes = [IsOwner]
        if self.action in ['create', 'destroy']:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

