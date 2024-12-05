from django.db import models

from solo.models import SingletonModel

from ckeditor.fields import RichTextField

class MainPage(SingletonModel):
    header_image = models.ImageField(blank=True, null=True)
    header_title = models.CharField(max_length=200, blank=True, null=True)
    chair_photo = models.ImageField(blank=True, null=True)
    chair_name = models.CharField(max_length=200, blank=True, null=True)
    chair_message = RichTextField()
    chair_signature = models.ImageField(blank=True, null=True)
    welcome_statement = RichTextField()
