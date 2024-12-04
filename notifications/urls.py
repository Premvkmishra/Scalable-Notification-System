from django.urls import path
from .views import RegisterUser, SendNotification

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register_user'),
    path('send/', SendNotification.as_view(), name='send_notification'),
]
