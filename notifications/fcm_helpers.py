import requests
from django.conf import settings

def send_fcm_notification(fcm_token, message):
    server_key = settings.FCM_DJANGO_SETTINGS['FCM_SERVER_KEY']
    url = 'https://fcm.googleapis.com/fcm/send'

    headers = {
        'Authorization': f'key={server_key}',
        'Content-Type': 'application/json',
    }

    payload = {
        'to': fcm_token,
        'notification': {
            'title': 'New Notification',
            'body': message,
        }
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.json()
