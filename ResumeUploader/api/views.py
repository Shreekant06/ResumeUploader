from django.shortcuts import render
from rest_framework.response import Response
from .models import Profile
from .serializer import ProfileSerializer
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.

