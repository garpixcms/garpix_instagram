from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import InstagramPost


@receiver(post_save, sender=InstagramPost)
def validate_username(sender, instance, *args, **kwargs):
    if '@' not in instance.user_name:
        instance.user_name = '@' + instance.user_name
        instance.save()
