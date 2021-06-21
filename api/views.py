from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, viewsets
from django.contrib.auth import get_user_model

from .serializers import UserSerializer


def placeholder(request):
    return HttpResponse('Placeholder')


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
