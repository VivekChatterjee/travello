from django.contrib import admin
from .models import Destination


# Register your models here.
# admin.site.register(Destination)

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc', 'price', 'offer']