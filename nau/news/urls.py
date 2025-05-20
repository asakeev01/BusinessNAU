from django.urls import path

from . import views

urlpatterns = [
    path("", views.news_list, name="news-list"),
    path("<int:pk>/", views.news_detail, name='news-detail'),
]