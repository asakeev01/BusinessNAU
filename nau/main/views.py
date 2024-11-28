from django.shortcuts import render

from .models import MainPage
from programs.models import Program

def main_page(request):
    main_page_content = MainPage.objects.first()
    programs = Program.objects.all()
    return render(request, 'main_page.html', {
        'main_page': main_page_content,
        'programs': programs,
    })
