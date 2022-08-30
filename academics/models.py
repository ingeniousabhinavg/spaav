from django.db import models

# Create your models here.

class AcademicsNews(models.Model):
    title = models.CharField(max_length=254)
    file = models.FileField(upload_to='anews', null=True)
    date = models.DateField('NewsDate')

    def __str__(self) -> str:
        return self.title

