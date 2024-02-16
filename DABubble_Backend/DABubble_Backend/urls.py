
from django.contrib import admin
from django.urls import path
from DABubble.views import RegisterView, LoginView, ProfileUpdateAPIView, CustomUserAPIView, LogoutView, GetAllUsersView, ChannelsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign_up/', RegisterView.as_view(), name='register'),
    path('sign_in/', LoginView.as_view(), name='login'),
    path('update_user/', ProfileUpdateAPIView.as_view(), name='update_user'),
    path('get_user/', CustomUserAPIView.as_view(), name='get_user'),
    path('log_out/', LogoutView.as_view(), name='log_out'),
    path('get_all_users/', GetAllUsersView.as_view(), name='allusers'),
    path('channel/', ChannelsView.as_view(), name='channel'),
]
