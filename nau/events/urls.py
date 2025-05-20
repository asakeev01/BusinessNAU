from django.urls import path

from . import views


urlpatterns = [
    path("", views.events_list, name="events-list"),
    path("<int:pk>/", views.event_detail, name='event-detail'),
]