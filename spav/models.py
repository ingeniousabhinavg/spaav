from distutils.command.upload import upload
from email.policy import default
from secrets import choice
from typing import Tuple
from unicodedata import name
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

class Achivements(models.Model):
    achiveTitle = models.CharField(max_length=200)
    aciveFile = models.FileField(upload_to='achivements')
    achiveUrl = models.URLField( max_length=200)
    achiveDate = models.DateField(auto_now=False, auto_now_add=False)
    
    def __str__(self) -> str:
        return self.achiveTitle



# Administration #
class BOG(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=300)
    designation_choices = (
        ('Director', 'Director'),
        ('Director in Charge', 'Director in Charge'),
        ('Dy Director', 'Dy Director'),
    )
    designation = models.CharField(max_length=100, choices=designation_choices)
    qualification = models.CharField(max_length=200)
    phone = models.CharField(max_length=40)
    email = models.EmailField(max_length=200)
    cv = models.FileField(upload_to='director/cv')
    image = models.ImageField(upload_to='director/profile')
    joinedOn = models.DateTimeField( blank=False)
    about = models.TextField()
    message = models.TextField()

    def __str__(self) -> str:
        return self.name

class Registrar(models.Model):
    pass

class Deans(models.Model):
    pass

# Administration #

# commitiees #
class NIRFCell(models.Model):
    pass

class StudentsGriveance(models.Model):
    pass

class VegilanceOfficer(models.Model):
    pass

class MentalHealth(models.Model):
    pass

class TranninPlacement(models.Model):
    pass

class UBA(models.Model):
    pass

class EBSB(models.Model):
    pass

# more will be added soon
# commitiees #