from django.shortcuts import render
from rest_framework import viewsets
from .models import Createuser
from .serializers import CreateuserSerializer


class CreateuserViewset(viewsets.ModelViewSet):
    queryset = Createuser.objects.all()
    serializer_class = CreateuserSerializer
