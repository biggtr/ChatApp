from django.conf import settings
from django.db import models

# Create your models here.


class ChatRoom(models.Model):
    name = models.CharField(max_length=50)
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self) -> str:
        return self.name


class Message(models.Model):
    text = models.TextField()
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    chat_room = models.ForeignKey(
        ChatRoom, on_delete=models.CASCADE, related_name="chat_room"
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text[:20]
