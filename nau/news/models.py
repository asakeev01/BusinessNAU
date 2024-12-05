from django.db import models

from ckeditor.fields import RichTextField

class News(models.Model):
    NEWS_CHOICES = [
        ('Latest', 'Latest'),
        ('Upcoming', 'Upcoming')
    ]
    image = models.ImageField(blank=True, null=True)
    type = models.CharField(max_length=10, choices=NEWS_CHOICES)
    name = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    header_image = models.ImageField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    content = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "News"

