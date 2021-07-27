from django.contrib import admin

from .models import (
    Nationality,
    Title,
    Applicant,
    IdentificationDocumentType,
    IdentificationDocument,
)


admin.site.register(Nationality)
admin.site.register(Title)
admin.site.register(Applicant)
admin.site.register(IdentificationDocument)
admin.site.register(IdentificationDocumentType)