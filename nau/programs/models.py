from django.db import models


class Program(models.Model):
    name = models.CharField(max_length=200)
    main_name = models.CharField(max_length=200)
    main_description = models.TextField()

    def __str__(self):
        return self.name


class HeaderImage(models.Model):
    image = models.ImageField()


class Slider(models.Model):
    program = models.OneToOneField(Program, on_delete=models.CASCADE)
    images = models.ManyToManyField(HeaderImage)

    def __str__(self):
        return f"{self.program.name}'s slider"


class Link(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    link = models.URLField(max_length=200)

    def __str__(self):
        return f"{self.program.name}'s link"


class Block(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f"{self.program.name}'s block"




