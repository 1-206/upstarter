from django.db import models


class Chat(models.Model):
    users = models.ManyToManyField('User', related_name='chats')


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(
        'User',
        related_name='messages',
        on_delete=models.DO_NOTHING,
    )

    def __str__(self):
        return f'{self.text[:20]}'
