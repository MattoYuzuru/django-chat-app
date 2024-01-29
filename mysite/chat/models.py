from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    participants = models.ManyToManyField(User, related_name='chats')

    def __str__(self):
        return ', '.join([str(participant) for participant in self.participants.all()])


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender}: {self.content}'
