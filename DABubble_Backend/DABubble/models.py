from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        user = self.create_user(email, password, **extra_fields)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    email_confirmed = models.BooleanField(default=False)
    password_reset_token_used = models.BooleanField(default=False)
    name = models.CharField(max_length=100, default='', blank=False, null=False)
    objects = CustomUserManager()
    avatar = models.CharField(max_length=100,  null=True, blank=True)
    USERNAME_FIELD = 'email'
    chats = models.ManyToManyField('Chat', related_name='users', null=True, blank=True)
    
    
class Message(models.Model):
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE)
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  
    emoji = models.CharField(max_length=100, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)  

class Chat(models.Model): 
    chat_id = models.IntegerField(unique=True) 
    messages = models.ManyToManyField(Message, related_name='chats')
   

class Channel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    members = models.ManyToManyField(CustomUser, related_name='channels')  
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, null=True, blank=True)  
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_channels')
    created_at = models.DateTimeField(auto_now_add=True)
    
