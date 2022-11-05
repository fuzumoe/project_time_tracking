from rest_framework import serializers

from project_time_tracking.api.models.project import Project
from project_time_tracking.api.serializers.project_meta import ProjectMemberSerializer
from project_time_tracking.api.serializers.user import UserSerializer
from project_time_tracking.api.serializers.project_meta import TaskSerializer


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    members = ProjectMemberSerializer(read_only=True, many=True, allow_null=True, )
    owner = UserSerializer(read_only=True, many=False, allow_null=True, )
    tasks = TaskSerializer(read_only=True, many=True, allow_null=True, )

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'owner', 'members', 'tasks', 'num_of_members', 'created_at', ]
        read_only_fields = ['id', 'owner', 'members', 'tasks', ]
        depth = 1
