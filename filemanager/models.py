from django.db import models
from datetime import date



class Data(models.Model):
    file_id = models.AutoField(primary_key=True)
    file = models.FileField(null=True, max_length=255)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.file.name)
