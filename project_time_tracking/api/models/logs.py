from django.db import models

class TaskLog(models.Model):
    task = models.ManyToManyField(to='api.Task',)
    log = models.TextField(blank=True, null=True)
