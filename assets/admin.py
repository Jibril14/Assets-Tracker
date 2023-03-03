from django.contrib import admin

from .models import Assets, AssetLogs, Category

admin.site.register(Assets)
admin.site.register( AssetLogs)
admin.site.register(Category)