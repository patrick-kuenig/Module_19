from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Game)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size', 'description',)
