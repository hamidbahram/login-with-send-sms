from django.contrib import admin
from .models import profile
# Register your models here.
@admin.register(profile)
class AdminProfile(admin.ModelAdmin):
    pass