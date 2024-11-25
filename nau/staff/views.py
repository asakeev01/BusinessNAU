from django.shortcuts import render

from .models import StaffMember


def index(request):
    staff_list = StaffMember.objects.all()
    context = {"staff_list": staff_list}
    print(context)
    print("********")
    return render(request, "staff/staff_list.html", context)
