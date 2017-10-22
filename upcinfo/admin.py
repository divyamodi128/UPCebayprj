from django.contrib import admin
from .models import UPCProduct

class UPCProductAdmin(admin.ModelAdmin):
    list_display = ('prodid', 'title', 'price', 'extra_fields')
    list_display_links = ('prodid',)

admin.site.register(UPCProduct, UPCProductAdmin)