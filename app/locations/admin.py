from django.contrib import admin

from .models import District, Quarter, Community


admin.site.register(District)
admin.site.register(Quarter)
admin.site.register(Community)