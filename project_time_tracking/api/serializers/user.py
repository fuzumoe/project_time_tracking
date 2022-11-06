from rest_framework import serializers

from project_time_tracking.api.models.user import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'full_name', 'email', 'is_superuser', 'is_staff', 'is_active', 'date_joined', ]
        read_only_fields = ['url', 'id', ]

    def update(self, instance, validated_data):
        if self.context["request"].method == 'PATCH':
            instance.email = validated_data.get("email", instance.email)
            instance.full_name = validated_data.get("full_name", instance.full_name)
            instance.is_active = validated_data.get("is_active", instance.is_active)
        if self.context["request"].method == 'PUT':
            instance.email = validated_data.get("email", instance.email)
            instance.full_name = validated_data.get("full_name", instance.full_name)
            instance.is_active = validated_data.get("is_active", instance.is_active)
            instance.is_superuser = validated_data.get("is_superuser", instance.is_superuser)
            instance.is_staff = validated_data.get("is_staff", instance.is_staff)
            instance.date_joined = validated_data.get("date_joined", instance.date_joined)

        instance.save()
        return instance
