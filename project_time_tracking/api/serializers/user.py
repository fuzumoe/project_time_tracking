from rest_framework import serializers

from project_time_tracking.api.models.user import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'is_staff', 'is_active', 'date_joined', ]
        read_only_fields = ['id', ]
