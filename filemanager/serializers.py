from rest_framework import serializers
from .models import Data
from django.utils import timezone
# Import Datetime
from datetime import datetime

#Often you'll want serializer classes that map closely to Django model definitions.
# The ModelSerializer class provides a shortcut that lets you automatically create
#  a Serializer class with fields that correspond to the Model fields.

class DataSerializer(serializers.ModelSerializer):

    size = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    filetype = serializers.SerializerMethodField()
    since_added = serializers.SerializerMethodField()

    class Meta:
        model = Data
        # fields = '__all__'
        fields = ('file_id', 'file', 'since_added', 'size', 'name', 'filetype')

    # def create(self, validated_data):
    #     print(validated_data)
    #     updata = self.context.get('files')
    #     name = validated_data.get('name', None)
    #     print(name)
    #     # size = validated_data.get('size', None)
    #     return Data.objects.create(data=updata)
    #     # return Data(data=updata)
        # return str(number_of_bytes) + ' ' + unit

    def get_size(self, obj):
        # request = self.context.get('request')
        file_size = ''
        if obj.file and hasattr(obj.file, 'size'):
            file_size = obj.file.size
        # size_converted = self.convert_size(file_size)
        # return size_converted
        return file_size

    def get_name(self, obj):
        file_name = ''
        if obj.file and hasattr(obj.file, 'name'):
            file_name = obj.file.name
        return file_name

    def get_filetype(self, obj):
      filename = obj.file.name
      return filename.split('.')[-1]

    def get_since_added(self, obj):
        date_added = obj.date_created
        return date_added
