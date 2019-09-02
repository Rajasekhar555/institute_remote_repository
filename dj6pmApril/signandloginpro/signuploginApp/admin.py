from django.contrib import admin

from .models import SignUpData

class AdminSignUpData(admin.ModelAdmin):
    list_display = ['username']


admin.site.register(SignUpData,AdminSignUpData)
