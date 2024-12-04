from django.db import models

from solo.models import SingletonModel

class MainPage(SingletonModel):
    header_image = models.ImageField()
    header_title = models.CharField(max_length=200)
