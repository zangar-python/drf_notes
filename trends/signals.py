from django.conf import settings
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import Trend
from .botV2 import BotV2

@receiver(post_save,sender=Trend)
def TrendSaved(sender,instance,created,**kwargs):
    if created:
        print(BotV2().created_trend(instance))

@receiver(post_delete,sender=Trend)
def TrendDeleted(sender,instance,**kwargs):
    print(BotV2().deleted_trend(instance))