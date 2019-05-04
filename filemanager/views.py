from django.shortcuts import render
from rest_framework import generics
from .models import Data
from .serializers import DataSerializer

# from rest_framework.views import APIView
# from rest_framework.response import Response
#
# from rest_framework import permissions, status
#
# from rest_framework.parsers import FileUploadParser, MultiPartParser, JSONParser, FormParser
# import os
#
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
#
# class FileUploadView(APIView):
#     permission_classes = (permissions.AllowAny,)
#     parser_classes = (MultiPartParser, FormParser )
#
#
#     def post(self, request, format=None):
#         print(request.data['file'].name)
#         print(dir(request.FILES['file']))
#         serializer = DataSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
