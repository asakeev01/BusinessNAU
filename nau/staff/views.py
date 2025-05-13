from django.shortcuts import render

from .models import *


def index(request):
    staff_list = StaffMember.objects.all()
    config = StaffPageConfig.get_solo()
    context = {
        "staff_list": staff_list,
        "config": config
    }
    return render(request, "staff/staff_list.html", context)
