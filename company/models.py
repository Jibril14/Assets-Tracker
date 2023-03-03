from django.db import models

class Company(models.Model):
    company_id = models.BigAutoField(primary_key=True, editable=False)
    company_name=models.CharField(max_length=150)

    class Meta:
        verbose_name = 'company'
        verbose_name_plural = 'companies'

    def __str__(self):
        return self.company_name
