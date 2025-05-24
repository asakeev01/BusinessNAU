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
    header_image = models.ImageField(blank=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    flyer = models.ImageField()
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    speaker = models.CharField(max_length=255, blank=True)
    speaker_link = models.URLField(max_length=200, blank=True)


class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    image = models.ImageField()


class EventVideo(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    video = models.FileField()


