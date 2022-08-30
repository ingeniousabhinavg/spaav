from django.contrib import admin
from spav.models import FlashNews, Logos, Noticeboard, Faculty

# Register your models here.

admin.site.register(Faculty)
admin.site.register(Noticeboard)
admin.site.register(Logos)
admin.site.register(FlashNews)