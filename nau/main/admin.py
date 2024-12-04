from django.contrib import admin

from .models import *
from solo.admin import SingletonModelAdmin


admin.site.register(MainPage, SingletonModelAdmin)
