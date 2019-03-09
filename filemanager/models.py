from django.db import models
from django.utils import timezone

class Data(models.Model):
    file_id = models.AutoField(primary_key=True)
    file = models.FileField(null=True, max_length=255)
    date_created = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return str(self.file.name)
