from multiprocessing import context
from django.shortcuts import render
from .models import Tender, Faculty, Noticeboard, Logos, FlashNews, Achivements, Director, BWC
from django.core.paginator import Paginator
# Call the objects 

flash_news = FlashNews.objects.all().order_by('-date')
logos = Logos.objects.all()
facultyData = Faculty.objects.all()
directorData = Director.objects.all()

# Create your views here.

context = {
    'flash_news': flash_news,
    'logos':logos,
    'facultyData':facultyData,
    'Director':directorData
}


def index(request):
    return render(request, 'index.html', context)

def planning(request):
    return render(request, 'dop.html', context)

def director(request):
    return render(request, 'director.html', context)

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

def tender(request):
    tenderData = Tender.objects.all()
    paginator = Paginator(tenderData, 3)
    page_number = request.GET.get('page')
    final_tender = paginator.get_page(page_number)
    total_pages = final_tender.paginator.num_pages
    last_page = final_tender.paginator.num_pages
    tenderDict = {
    'tenderData':final_tender,
    'total_pages':[n+1 for n in range(total_pages)],
    'last_page':last_page
    }
    return render(request, 'tender.html',tenderDict)

def about(request):
    return render(request, 'about.html')

def achivements(request):
    achivementsData = Achivements.objects.all()
    paginator = Paginator(achivementsData, 3)
    page_number = request.GET.get('page')
    final_achivementData = paginator.get_page(page_number)
    total_page = final_achivementData.paginator.num_pages
    last_page = final_achivementData.paginator.num_pages
    achiveDict ={
        'achivementsData':achivementsData,
        'total_pages':[n+1 for n in range(total_page)],
        'last_page':last_page
    }
    return render(request, 'achivements.html', achiveDict)

def bog(request):
    return render(request, 'bog.html')

def commitee(request):
    return render(request, 'commitee.html')

def bwc(request):
    bwcData = BWC.objects.all()
    bwc={
        'bwcData':bwcData
    }
    return render(request, 'admin/bwc.html',bwc)


def rti(request):
    return render(request, 'rti.html')

def gallery(request):
    return render(request,  'gallery.html')

def screen(request):
    return render(request, 'screen_reader.html')

def policies(request):
    return render(request,  'policies.html')

