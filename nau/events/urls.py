from django.urls import path

from . import views


urlpatterns = [
    path("", views.event_types_list, name='event-types-list'),
    path("type/<int:type_id>/", views.event_type_detail, name='event-type-detail'),
    path("<int:pk>/", views.event_detail, name='event-detail'),

]