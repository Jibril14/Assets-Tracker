from django.db import models

from django.conf import settings

class Company(models.Model):
    company_name= models.CharField(max_length=150)
  
    class Meta:
        verbose_name = 'company'
        verbose_name_plural = 'companies'

    def __str__(self):
        return self.company_name
