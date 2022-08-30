from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import AcademicsNews
from django.core.paginator import Paginator

# Call your data from models



# context of the data to be sent on the page


# Create your views here.

def index(request):
    AcademicsnewsData = AcademicsNews.objects.all().order_by('-date')
    paginator = Paginator(AcademicsnewsData, 10)
    page_number = request.GET.get('page')
    final_news = paginator.get_page(page_number)
    total_pages = final_news.paginator.num_pages
    last_page = final_news.paginator.num_pages
    context = {
    'AcademicsNews_data':final_news,
    'total_pages':[n+1 for n in range(total_pages)],
    'last_page':last_page
    }
    return render(request, 'academics.html', context)