from django.conf import settings
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver


from .models import Chat,Message
from .botV1 import BotV1

@receiver(post_save,sender=Chat)
def SendMessage(sender,instance,created,**kwargs):
    if created:
        BotV1("noname").sendMessage_CreatedChat(instance.id)
        print(f"BOTV1 SEND MASSAGE TO CHAT ID:{instance.id}")
        
@receiver(post_delete,sender=Chat)
def ChatDeleted_sendMessage(sender,instance,**kwargs):
    print("Chat is deleted")
    print("BotV1 is activated")
    print(f"Chat '{instance}' is null,BotV1 is deactived")

@receiver(post_save,sender=Message)
def SendHelloBotV1(sender,instance,created,**kwargs):
    if created:
        if instance.from_user == BotV1("noname").NAME_OF_BOT:
            return 
        BotV1(user=instance.from_user).hello_user(instance.chat.id,instance.text)
        