from django.shortcuts import render
from rest_framework.decorators import api_view

from accounts.serializers import UserSerializer
from rest_framework.response import Response

@api_view(['POST'])
def register(request):
    data = request.data 
    serializer = UserSerializer(data=data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    

@api_view(['GET'])
def me(request):

    user = request.user
    serializer = UserSerializer(user)

    return Response(serializer.data)