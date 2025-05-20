from django.contrib import admin

from .models import *

from solo.admin import SingletonModelAdmin


admin.site.register(Event)
admin.site.register(EventType)
admin.site.register(EventImage)
admin.site.register(EventVideo)
admin.site.register(EventsPageConfig, SingletonModelAdmin)
