from django.db import models
from datetime import date



class Data(models.Model):
    # filename = models.CharField(max_length=250)
    data_id = models.AutoField(primary_key=True)
    data = models.FileField(null=True, max_length=255)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.data.name)

# class FileType(models.Model):
#     data_type = models.ForeignKey(Data, related_name='types', on_delete=models.CASCADE)





