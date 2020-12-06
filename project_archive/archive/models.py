from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Archive(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    project_file = models.FileField(upload_to="project_files/")
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_uploaded = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title[:50]}"
