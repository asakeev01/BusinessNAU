from django.shortcuts import render

from .models import MainPage
from programs.models import Program
from news.models import News
from staff.models import StaffPageConfig

def main_page(request):
    main_page_content = MainPage.get_solo()
    programs = Program.objects.all()
    upcoming_news = News.objects.filter(type='Upcoming').order_by('-id')[:3]
    staff_page = StaffPageConfig.get_solo()
    return render(request, 'main/main_page.html', {
        'main_page': main_page_content,
        'programs': programs,
        'upcoming_news': upcoming_news,
        'staff_page': staff_page
    })
