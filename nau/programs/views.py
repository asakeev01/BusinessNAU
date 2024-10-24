from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, program_id):
    return HttpResponse("You're looking at program %s." % program_id)

