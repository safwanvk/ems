from django.shortcuts import render

from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework import generics
from django.contrib.auth.models import User

# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer