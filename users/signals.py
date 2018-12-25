from django.db.models.signals import post_save
from django.contrib.auth.models import User #sending save signal
from django.dispatch import receiver #recieve signals
from .models import Profile

@receiver(post_save, sender=User) #When user object is saved send this function
def create_profile(sender, instance, created, **kwargs): #?
    if created: #if user is created
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs): #?
    instance.profile.save() #save user profile
