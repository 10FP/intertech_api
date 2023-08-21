from django.shortcuts import render
from rest_framework import viewsets
from .models import IdCardPhoto
from .serializers import IdCardPhotoSerializer


class IdCardPhotoViewset(viewsets.ModelViewSet):
    queryset = IdCardPhoto.objects.all()
    serializer_class = IdCardPhotoSerializer
