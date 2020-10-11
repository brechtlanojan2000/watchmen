from django.contrib import admin

from .models import Brand, Watch, WatchImage

# Register your models here.

admin.site.register(Brand)
admin.site.register(Watch)
admin.site.register(WatchImage)