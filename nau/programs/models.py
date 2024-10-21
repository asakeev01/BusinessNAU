from django.db import models


class Program(models.Model):
    name = models.CharField(max_length=200)

class HeaderImage(models.Model):
    image = models.ImageField()


class Slider(models.Model):
    program = models.OneToOneField(Program, on_delete=models.CASCADE)
    images = models.ManyToManyField(HeaderImage)


class Link(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    link = models.URLField(max_length=200)


class Block(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField()




