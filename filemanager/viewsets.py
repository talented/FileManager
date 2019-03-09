from rest_framework import viewsets
from .models import Data
from .serializers import DataSerializer
from rest_framework.response import Response # from viewsets doc
from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework import permissions, status

from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser

# A ViewSet class is simply a type of class-based View,
# that does not provide any method handlers such as .get() or .post(),
# and instead provides actions such as .list() and .create().

# Typically, rather than explicitly registering the views in a viewset
# in the urlconf, you'll register the viewset with a router class,
# that automatically determines the urlconf for you.

class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

    permission_classes = (permissions.AllowAny,) # we assume that we have a session user
    parser_classes = (MultiPartParser, FormParser )

    def post(self, request, format=None):
        # print(request.data['file'].name)
        # print(dir(request.FILES['file']))
        serializer = DataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            for k, v in kwargs.items():
                for id in v.split(','):
                    obj = get_object_or_404(Data, pk=int(id))
                    self.perform_destroy(obj)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)
