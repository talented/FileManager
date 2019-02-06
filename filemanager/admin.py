from django.contrib import admin
from .models import Data

class DataAdmin(admin.ModelAdmin):
    fields = ('name', 'size', 'date_created')


# Register your models here.
admin.site.register(Data, DataAdmin)
