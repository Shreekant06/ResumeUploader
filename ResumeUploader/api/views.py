from django.shortcuts import render
from rest_framework.response import Response
from .models import Profile
from .serializer import ProfileSerializer
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
class ProfileView(APIView):

    #method to post data 
    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'msg' : 'Resume Uploaded Successfully',
                'status' : 'Success', 'candidate' : serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    

    #method to get data
    def get(self, request, format=None):
        candidate = Profile.objects.all()
        serializer = ProfileSerializer(candidate, many=True)
        return Response({
            'status' : 'Success', 'candidate' : serializer.data
        }, status=status.HTTP_200_OK)

    
