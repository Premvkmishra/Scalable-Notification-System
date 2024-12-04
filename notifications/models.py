from django.db import models



class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    device_type = models.CharField(max_length=50)  # e.g., 'android', 'ios'
    fcm_token = models.TextField()  # Token for FCM


    class Meta:
        app_label = 'notifications'

    def __str__(self):
        return self.username

class NotificationLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    status = models.CharField(max_length=50)  # e.g., 'success', 'failed'
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification to {self.user.username} - {self.status}"
