from django.contrib import admin

from .models import *

from solo.admin import SingletonModelAdmin


admin.site.register(News)
admin.site.register(NewsPageConfig, SingletonModelAdmin)
