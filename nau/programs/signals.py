from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Program, Slider


@receiver(post_save, sender=Program)
def create_slider(sender, instance, created, **kwargs):
    if created:
        Slider.objects.create(program=instance)
