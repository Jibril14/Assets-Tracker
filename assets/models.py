from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from company.models import Company
import datetime


User = get_user_model()
# Create your models here.

class Assets(models.Model):
    name = models.CharField(max_length=150)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True,)
    availability = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey("Category", default=1, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'asset'
        verbose_name_plural = 'assets'

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name
    

class AssetLogs(models.Model):
    class Conditions(models.TextChoices):
        NEW = "NEW", _('New')
        FAIRLY_USED = "FAIRLY_USED", _("Fairly_Used")

    asset = models.ForeignKey('Assets', on_delete=models.CASCADE, null=True,)
    collected_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True )
    condition = models.CharField(max_length=20, choices=Conditions.choices, default=Conditions.NEW)
    check_out = models.DateTimeField(auto_now_add=True, blank=True)
    return_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['asset']
        verbose_name = 'assets_log'
        verbose_name_plural = 'assets_logs'
    

class Category(models.Model):
    category_name = models.CharField(max_length=100,  verbose_name=_("Category Name"), unique=True)
    description = models.CharField(max_length=255, verbose_name=_("Description"), blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name
