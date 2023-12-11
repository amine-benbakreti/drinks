from django.shortcuts import render
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from django.db.models.signals import pre_save


@api_view(['POST'])
def signUpUser(request):
    try:
        data = request.data
        user = User.objects.create(
            username = data['username'],
            email = data['email'],
            password =  make_password(data['password']),
            first_name = data['first_name']
        )
        serializer = UserSerializer(user, many=False)

        return Response(serializer.data)
    except:
        message = {
            "details": "User with this email already exist"
        }
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUser(request):

    user = request.user
    serialized = UserSerializer(user, many=False)

    return Response(serialized.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def getUsers(request):

    users = User.objects.all()
    serializer = UserSerializer(users, many=True)

    return Response(serializer.data)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):

        token = super().get_token(user)
        token['email'] = user.email
        token['first_name'] = user.first_name

        return token


    def validate(self, attrs):

        data = super().validate(attrs)
        data['email'] = self.user.email
        data['username'] = self.user.username
        data['token'] = self.get_token(user)

        return data

class MyTokenObtainedPairView(TokenObtainPairView):

    serializer_class = MyTokenObtainPairSerializer