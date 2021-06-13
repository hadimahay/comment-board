from django.contrib import admin
from .models import board
# Register your models here.
@admin.register(board)
class bordadmin(admin.ModelAdmin):
    list_display = ['comment','created_at','updated_at']
    TimeField = ('created_at',)