from rest_framework import serializers
from .models import Data
# import datetime
from django.utils import timezone

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

    def convert_size(self, size):
        #2**10 = 1024
        power = 2**10
        n = 0
        powerN = {0 : 'B', 1: 'KB', 2: 'MB', 3: 'GB', 4: 'TB'}
        while size > power:
            size /=  power
            n += 1

        precision = 1
        size = round(size, precision)

        return str(size) + ' ' + powerN[n]
        # return size, Dic_powerN[n]+'bytes'

        # step_to_greater_unit = 1024.
        #
        # number_of_bytes = float(number_of_bytes)
        # unit = 'B'
        #
        # if (number_of_bytes / step_to_greater_unit) >= 1:
        #     number_of_bytes /= step_to_greater_unit
        #     unit = 'KB'
        #
        # if (number_of_bytes / step_to_greater_unit) >= 1:
        #     number_of_bytes /= step_to_greater_unit
        #     unit = 'MB'
        #
        # if (number_of_bytes / step_to_greater_unit) >= 1:
        #     number_of_bytes /= step_to_greater_unit
        #     unit = 'GB'
        #
        # if (number_of_bytes / step_to_greater_unit) >= 1:
        #     number_of_bytes /= step_to_greater_unit
        #     unit = 'TB'

        precision = 1
        number_of_bytes = round(number_of_bytes, precision)

        return str(number_of_bytes) + ' ' + unit

    def get_size(self, obj):
        # request = self.context.get('request')
        file_size = ''
        if obj.file and hasattr(obj.file, 'size'):
            file_size = obj.file.size
        size_converted = self.convert_size(file_size)
        return size_converted

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
        now = timezone.now()
        time_difference = now - date_added
        print(str(time_difference))
        return str(time_difference).split(',')[0] + ' ago'
