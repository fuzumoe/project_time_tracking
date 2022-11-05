from django.db import models



class Project(models.Model):
    title = models.TextField(blank=False, null=True)
    description = models.TextField(blank=False, null=True)
    owner = models.ForeignKey(to='api.User', on_delete=models.DO_NOTHING, null=True)
    members = models.ForeignKey(to='api.ProjectMember', related_name='projects', on_delete=models.DO_NOTHING, null=True)
    tasks = models.ForeignKey(to='api.Task', related_name='tasks', on_delete=models.DO_NOTHING, null=True)
    num_of_members = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
