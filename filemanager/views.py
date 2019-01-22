from django.shortcuts import render
from rest_framework import generics
from .models import Data
from .serializers import DataSerializer


class PostRudView(generics.RetrieveUpdateDestroyAPIView):
    # lookup_field = 'id'
    serializer_class = DataSerializer



    def get_queryset(self):
        return Data.objects.all()

    def get_object(self):
        return Data.objects.get(id=self.kwargs.get('id'))
