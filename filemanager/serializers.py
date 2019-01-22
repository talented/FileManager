from rest_framework import serializers
from .models import Data

#Often you'll want serializer classes that map closely to Django model definitions.
# The ModelSerializer class provides a shortcut that lets you automatically create
#  a Serializer class with fields that correspond to the Model fields.

class DataSerializer(serializers.ModelSerializer):

    size = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    filetype = serializers.SerializerMethodField()

    class Meta:
        model = Data
        # fields = '__all__'
        fields = ('data_id', 'data', 'name', 'filetype', 'size', 'date_created')

    def get_size(self, obj):
        # request = self.context.get('request')
        if obj.data and hasattr(obj.data, 'size'):
            file_size = obj.data.size
        return file_size

    def get_name(self, obj):
        if obj.data and hasattr(obj.data, 'name'):
            file_name = obj.data.name
        return file_name

    def get_filetype(self, obj):
      filename = obj.data.name
      return filename.split('.')[-1]



