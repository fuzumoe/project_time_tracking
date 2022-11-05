from django.db import models

from project_time_tracking.api.utils import validators

ENROLLED = 'enrolled'
PENDING = 'pending'

TODO = 'todo'
DONE = 'done'
INPROGRESS = 'inprogress'
COMPLETED = 'complted'

def zero_value():
    return 0

class ProjectMember(models.Model):
    CHOICES_STATUS = (
        (PENDING, 'Pending'),
        (ENROLLED, 'Enrolled')
    )
    member = models.ManyToManyField(to='api.User', )
    project = models.ManyToManyField(to='api.Project', )
    enrollment_status = models.CharField(max_length=200, choices=CHOICES_STATUS, default=PENDING, null=True)

    class Meta:
        app_label = "api"


class Task(models.Model):
    CHOICES_STATUS = (
        (TODO, 'Todo'),
        (DONE, 'Done'),
        (INPROGRESS, 'Inprogress'),
        (COMPLETED, 'Complted')
    )
    project = models.ManyToManyField(to='api.Project',)
    logs = models.ForeignKey(to='api.TaskLog', related_name="logs", on_delete=models.DO_NOTHING, null=True)
    description = models.TextField(blank=False, null=False)
    time_required = models.TextField(blank=False, null=False, validators=[validators.validate_time_data])
    time_spent = models.TextField(blank=False, null=False, validators=[validators.validate_time_data])
    status = models.CharField(max_length=200, choices=CHOICES_STATUS, default=TODO)
    created_at = models.DateTimeField(auto_now_add=True)

