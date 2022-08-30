from multiprocessing import context
from django.shortcuts import render
from .models import FlashNews, Logos, Noticeboard,Faculty
from django.core.paginator import Paginator
# Call the objects 

flash_news = FlashNews.objects.all().order_by('-date')
logos = Logos.objects.all()
facultyData = Faculty.objects.all()

# Create your views here.

context = {
    'flash_news': flash_news,
    'logos':logos,
    'facultyData':facultyData,
}


def index(request):
    return render(request, 'index.html', context)

def planning(request):
    return render(request, 'dop.html', context)

def noticeboard(request):
    noticeData = Noticeboard.objects.all()
    paginator = Paginator(noticeData, 10)
    page_number = request.GET.get('page')
    final_notice = paginator.get_page(page_number)
    total_pages = final_notice.paginator.num_pages
    last_page = final_notice.paginator.num_pages
    dataDict = {
    'noticeData':final_notice,
    'total_pages':[n+1 for n in range(total_pages)],
    'last_page':last_page
    }
    return render(request, 'noticeboard.html',dataDict)

def screen(request):
    return render(request, 'screen_reader.html')

def rti(request):
    return render(request, 'rti.html')

def gallery(request):
    return render(request,  'gallery.html')

def policies(request):
    return render(request,  'policies.html')

