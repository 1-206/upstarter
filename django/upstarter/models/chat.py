from django.db import models
from .user import User



class Chat(models.Model):
    users = models.ManyToManyField(User, related_name='chats')


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.DO_NOTHING)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
