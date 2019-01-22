from rest_framework import viewsets
from .models import Data
from .serializers import DataSerializer
from rest_framework.response import Response # from viewsets doc
from django.shortcuts import get_object_or_404

# A ViewSet class is simply a type of class-based View,
# that does not provide any method handlers such as .get() or .post(),
# and instead provides actions such as .list() and .create().

# Typically, rather than explicitly registering the views in a viewset
# in the urlconf, you'll register the viewset with a router class,
# that automatically determines the urlconf for you.

class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer


# class DataViewSet(viewsets.ViewSet):


#     def list(self, request, pk=None):
#         # queryset = Data.objects.all()
#         # serializer = DataSerializer(queryset, many=True)
#         # return Response(serializer.data)
#         querysets = Data.objects.all()
#         size = []
#         for queryset in querysets:
#             size.append(queryset.data.size)
#         file_size = get_object_or_404(size, pk=pk)
#         serializer = DataSerializer(file_size)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = Data.objects.all()
#         filedata = get_object_or_404(queryset, pk=pk)
#         serializer = DataSerializer(filedata)
#         return Response(serializer.data)

#     def get_custom(self, request, pk=None):
#         queryset = Data.objects.all()
#         for query in queryset:
#             size = query.data.size
#         file_size = get_object_or_404(size, pk=pk)
#         serializer = DataSerializer(file_size)
#         return Response(serializer.data)


