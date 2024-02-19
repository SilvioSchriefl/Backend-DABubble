
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .serializers import RegistrationSerializer, LoginSerializer, CustomUserSerializer, ChannelSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser, Channel
from django.contrib.auth import authenticate, logout
from rest_framework.authtoken.models import Token


class RegisterView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'detail': 'User successfully created'},  status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                return Response({
            'token': token.key,
            'id': user.pk,
            'email': user.email,
            'name': user.name,
            'avatar': user.avatar,
            'active': user.is_active,
            }, status=status.HTTP_200_OK)
            else:
                return Response({'details': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProfileUpdateAPIView(APIView):

    def post(self, request):
        user = request.user
        data = request.data
        serializer = CustomUserSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CustomUserAPIView(APIView):
    
    def get(self, request):
        user = request.user
        if user:
            return Response({
                'id': user.pk,
                'email': user.email,
                'name': user.name,
                'avatar': user.avatar
            })
        else:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
class GetAllUsersView(APIView):
    
    def get(self, request):
        if request.user.is_authenticated:
            users = CustomUser.objects.all()
            serializer = CustomUserSerializer(users, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        
        
class LogoutView(APIView):

    def post(self, request):
        if request.user.is_authenticated:
            Token.objects.filter(user=request.user).delete()
            logout(request)
            return Response({"message": "successfully logged out."}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Authentication credentials were not provided."},
                            status=status.HTTP_401_UNAUTHORIZED)
            
class ChannelsView(APIView):

    def post(self, request):
        serializer = ChannelSerializer(data=request.data)
        if serializer.is_valid():
            creator = request.user  
            serializer.save(creator=creator)
            member_ids = request.data.get('members', [])
            channel = serializer.save()
            channel.members.set(member_ids) 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        if request.user.is_authenticated:
            channels = Channel.objects.all()
            serializer = ChannelSerializer(channels, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        
    def patch(self, request):
        if request.user.is_authenticated: 
            channel_id = request.data.get('id')
            channel = get_object_or_404(Channel, pk=channel_id)
            members_data = request.data.get('members', [])  
            serializer = ChannelSerializer(instance=channel, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                if members_data is not None:
                    channel.members.set(members_data)
                    channel.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        
    def delete(self, request):
        if request.user.is_authenticated:
            channel_id = request.data.get('id')
            channel = get_object_or_404(Channel, pk=channel_id)
            channel.delete()
            return Response({'message': 'Channel deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        


        
