from django.contrib import admin
from .models import Dog

class DogAdmin(admin.ModelAdmin):
    pass
admin.site.register(Dog, DogAdmin)