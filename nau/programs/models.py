from django.db import models


class HeaderImage(models.Model):
    image = models.ImageField()


class Link(models.Model):
    link = models.URLField(max_length=200)





