from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("programs/", include("programs.urls")),
    path("staff/", include("staff.urls")),
    path("news/", include("news.urls")),
    path("main/", include("main.urls"))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
