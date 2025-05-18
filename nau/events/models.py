from django.db import models

from solo.models import SingletonModel


class EventsPageConfig(SingletonModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    header_image = models.ImageField()

    def __str__(self):
        return "Site Configuration"


class EventType(models.Model):
    name = models.CharField(max_length=255)


class Event(models.Model):
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    flyer = models.ImageField()
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    place = models.CharField(max_length=255)
    speaker = models.CharField(max_length=255)
    speaker_link = models.URLField(max_length=200)


class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    image = models.ImageField()


class EventVideo(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    video = models.FileField()


