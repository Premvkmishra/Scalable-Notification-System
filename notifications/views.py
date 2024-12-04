from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, NotificationLog
from .serializers import UserSerializer
from .fcm_helpers import send_fcm_notification

class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SendNotification(APIView):
    def post(self, request):
        device_type = request.data.get('device_type')
        message = request.data.get('message')

        users = User.objects.filter(device_type=device_type)
        for user in users:
            try:
                response = send_fcm_notification(user.fcm_token, message)
                NotificationLog.objects.create(user=user, message=message, status=response.get('success', 'failed'))
            except Exception as e:
                NotificationLog.objects.create(user=user, message=message, status=f"failed - {str(e)}")

        return Response({'message': 'Notifications sent'}, status=status.HTTP_200_OK)
