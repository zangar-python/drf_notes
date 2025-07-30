from django.db import models

# Create your models here.

class Chat(models.Model):
    chat_name =models.CharField(max_length=100,null=False)
    def __str__(self):
        return self.chat_name
class Message(models.Model):
    chat = models.ForeignKey(Chat,on_delete=models.CASCADE,related_name="messages")
    text = models.TextField(null=False)
    from_user = models.CharField(max_length=50)
    # to_user = models.CharField(max_length=50)
    def __str__(self):
        return self.from_user

class BotV1Model(models.Model):
    username = models.CharField(max_length=30,unique=True)
    info = models.TextField()
    auth_at = models.DateTimeField(auto_now_add=True)
    