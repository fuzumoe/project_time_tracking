from rest_framework import serializers

from project_time_tracking.api.models.project_meta import ProjectMember
from project_time_tracking.api.models.project_meta import Task
from project_time_tracking.api.serializers.logs import TaskLog
from project_time_tracking.api.serializers.user import UserSerializer
from project_time_tracking.api.serializers.project import ProjectSerializer


class ProjectMemberSerializer(serializers.HyperlinkedModelSerializer):
    member = UserSerializer(read_only=True, many=False, allow_null=True, )
    project = ProjectSerializer(read_only=True, many=False, allow_null=True, )

    class Meta:
        model = ProjectMember
        fields = ['url', 'id', 'member', 'project', 'enrollment_status', ]
        read_only_fields = ['id', 'member', 'project', ]
        depth = 1


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    logs = TaskLog(read_only=True, many=True, allow_null=True, )

    class Meta:
        model = Task
        fields = ['id', 'logs', 'description', 'time_required', 'time_spent', 'status', 'created_at', ]
        read_only_fields = ['id', 'logs']
        depth = 1
