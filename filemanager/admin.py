from django.contrib import admin
from .models import Data

class DataAdmin(admin.ModelAdmin):
    fields = ('data', 'date_created')


# Register your models here.
admin.site.register(Data, DataAdmin)

