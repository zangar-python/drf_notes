from .models import Message,Chat
from django.shortcuts import get_object_or_404
from user.models import CustomUser

class BotV1():
    def __init__(self,user):
        self.user = user
        
    NAME_OF_BOT = "BotV1"
    
    def hello_user(self,chat_id,text):
        if "/BotV1" in text:
            chat = get_object_or_404(Chat,pk=chat_id)
            if "users[]" in text:
                users = CustomUser.objects.all()
                str_users = "[-"
                for user in users:
                    str_users += f"{user.email}   00 {user.id};\n"
                str_users += "-]"
                
                Message.objects.create(chat=chat,text = str_users,from_user = self.NAME_OF_BOT) 
                print("BotV1 send message!") 
                return
            # print(type(chat_id))
            chat = get_object_or_404(Chat,pk=chat_id)
            message = Message.objects.create(chat=chat,text=f"Hello,{self.user}!",from_user=self.NAME_OF_BOT)
            message.save()
            print("BotV1 send message!")
            return
    def sendMessage_CreatedChat(self,chat_id):
        chat = get_object_or_404(Chat,pk=chat_id)
        text = "Hello,chat is created!"
        message = Message.objects.create(chat=chat,text=text,from_user=self.NAME_OF_BOT)
        message.save()
        return
    