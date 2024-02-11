from django.contrib import admin
from .models import CustomUser, Message, Chat, Channel

class CustomUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Message)
admin.site.register(Chat)
admin.site.register(Channel)