from django.db import models

class MainPage(models.Model):
    header_image = models.ImageField()
    header_title = models.CharField()
