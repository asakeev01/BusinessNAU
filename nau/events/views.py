from django.shortcuts import render, get_object_or_404
from .models import Event, EventsPageConfig, EventType


def events_list(request):
    config = EventsPageConfig.get_solo()
    event_types = EventType.objects.all()
    events_by_type = {etype.name: Event.objects.filter(event_type=etype).order_by('-date') for etype in event_types}

    return render(request, 'events/events_list.html', {
        'config': config,
        'events_by_type': events_by_type,
    })


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    images = event.eventimage_set.all()
    videos = event.eventvideo_set.all()
    return render(request, 'events/event_detail.html', {
        'event': event,
        'images': images,
        'videos': videos,
    })
