from django.shortcuts import get_object_or_404, render

from .models import Program


def index(request):
    program_list = Program.objects.all()
    context = {"program_list": program_list}
    return render(request, "programs/index.html", context)


def detail(request, program_id):
    program = get_object_or_404(Program, id=program_id)

    images = program.slider.images.all() if hasattr(program, 'slider') else None

    context = {
        'program': program,
        'images': images
    }
    return render(request, 'programs/detail.html', context)

