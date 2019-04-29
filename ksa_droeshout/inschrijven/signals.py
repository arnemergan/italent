from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Leiding

@receiver(post_save,sender=User)
def create_leiding(sender,instance,created,**kwargs):
    if created:
        Leiding.objects.create(userid=instance)

def save_leiding(sender,instance,**kwargs):
    instance.Leiding.save()