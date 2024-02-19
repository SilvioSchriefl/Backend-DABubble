
from rest_framework import serializers
from .models import CustomUser, Channel

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'avatar', 'name',)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)  
        user.save()
        return user
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('is_active', 'name', 'email', 'avatar', 'id',)
        
class ChannelSerializer(serializers.ModelSerializer):
    
    members = CustomUserSerializer(many=True, read_only=True)
    creator = CustomUserSerializer(read_only=True)
    class Meta:
        model = Channel
        fields = ('name', 'description', 'members', 'chat', 'id', 'creator', 'created_at',)
        