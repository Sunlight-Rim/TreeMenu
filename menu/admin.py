from django.contrib import admin
from .models import MenusModel, MenusAdmin

# Register your models here.
admin.site.register(MenusModel, MenusAdmin)