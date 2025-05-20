from django.urls import path

from . import views

urlpatterns = [
    path("", views.programs_list, name="programs-list"),
    path("<int:program_id>/", views.program_detail, name="program-detail"),
]