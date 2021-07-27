from django.contrib import admin

from .models import (
    Application,
    ApplicationType,
    Easement,
    LandUse,
    Recommendation,
    Response,
    Comment,
)

admin.site.register(Application)
admin.site.register(ApplicationType)
admin.site.register(Easement)
admin.site.register(LandUse)
admin.site.register(Recommendation)
admin.site.register(Response)
admin.site.register(Comment)
