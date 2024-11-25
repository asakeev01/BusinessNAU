from django.contrib import admin

from .models import *
from solo.admin import SingletonModelAdmin


admin.site.register(StaffPageConfig, SingletonModelAdmin)
admin.site.register(StaffMember)
admin.site.register(Education)