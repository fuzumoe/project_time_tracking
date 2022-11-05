from rest_framework import serializers

from project_time_tracking.api.models.logs import TaskLog
from project_time_tracking.api.serializers.project_meta import TaskSerializer

class TaskLogSerializer(serializers.HyperlinkedModelSerializer):
    task = TaskSerializer(read_only=True, many=True, allow_null=True, )

    class Meta:
        model = TaskLog
        fields = ['id', 'title', ]
        read_only_fields = ['id', 'task', ]
        depth = 1
