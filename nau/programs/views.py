from django.shortcuts import get_object_or_404, render

from .models import Program


def index(request):
    program_list = Program.objects.all()
    context = {"program_list": program_list}
    return render(request, "programs/programs_list.html", context)


def detail(request, program_id):
    program = get_object_or_404(Program, id=program_id)

    images = program.slider.images.all() if hasattr(program, 'slider') else None
    links = program.link_set.all()
    blocks = program.block_set.all()

    context = {
        'program': program,
        'images': images,
        'links': links,
        'blocks': blocks,
    }
    return render(request, 'programs/program_detail.html', context)

