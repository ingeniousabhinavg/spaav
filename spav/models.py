from secrets import choice
from typing import Tuple
from django.db import models

# Create your models here.


class FlashNews(models.Model):
    newsTitle = models.CharField(max_length=254)
    newsLink = models.URLField(null=True, blank=True)
    newsFile = models.FileField(upload_to='news', null=True, blank=True)
    date = models.DateTimeField('datetime', null=True, blank=True)
    newsImg = models.ImageField(upload_to='news', null=True, blank=True)

    def __str__(self) -> str:
        return self.newsTitle

class Noticeboard(models.Model):
    noticeTitle = models.CharField(max_length=254)
    file = models.FileField(upload_to='noticeboard', null=False,blank=True)
    noticeUrl = models.URLField(max_length=254, null=True, blank=True)
    noticedate = models.DateTimeField('datetime', null=True, blank=True)

    def __str__(self) -> str:
        return self.noticeTitle

# rectification needed 
class Logos(models.Model):
    altTitle = models.CharField(max_length=254, null=True)
    logoUrl = models.URLField(max_length=254, null=True)
    logImg = models.ImageField(upload_to='logos', null=False)

    def __str__(self) -> str:
        return self.altTitle
# rectification needed 

class Faculty(models.Model):
    facultyName = models.CharField(max_length=254)
    facultyQualification = models.CharField(max_length=254)
    facultyPhone = models.CharField(max_length=254)
    DESIGNATION = (
        ('Director', 'Director'),
        ('Professor', 'Professor'),
        ('Associate Professor', 'Associate Professor'),
        ('Assistant Professor', 'Assistant Professor'),
    )
    facutyDesignation = models.CharField(max_length=100, choices=DESIGNATION)
    facultyCV = models.FileField(upload_to='faculty/cv')
    facultyImage = models.ImageField(upload_to = 'faculty/image')
    

    def __str__(self) -> str:
        return self.facultyName

class Tender(models.Model):
    tenderTitle = models.CharField(max_length=254)
    tenderFile = models.FileField(upload_to='tender', null=False)
    tenderLastDate = models.DateTimeField('datetime', blank=False)

    def __str__(self) -> str:
        return self.tenderTitle