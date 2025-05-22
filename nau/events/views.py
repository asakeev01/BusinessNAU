from django.shortcuts import render, get_object_or_404
from .models import *


def event_types_list(request):
    config = EventsPageConfig.get_solo()
    event_types = EventType.objects.all()

    event_type_data = []
    for etype in event_types:
        latest_event = Event.objects.filter(event_type=etype).order_by('-date').first()
        images = EventImage.objects.filter(event=latest_event)[:3] if latest_event else []
        event_type_data.append({
            'type': etype,
            'images': images,
            'event_id': latest_event.id if latest_event else None
        })

    return render(request, 'events/event_types_list.html', {
        'config': config,
        'event_type_data': event_type_data
    })


def event_type_detail(request, type_id):
    event_type = get_object_or_404(EventType, id=type_id)
    events = Event.objects.filter(event_type=event_type).order_by('-date')
    return render(request, 'events/event_type_detail.html', {
        'event_type': event_type,
        'events': events
    })


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    images = EventImage.objects.filter(event=event)
    videos = event.eventvideo_set.all()
    return render(request, 'events/event_detail.html', {
        'event': event,
        'images': images,
        'videos': videos,
    })
