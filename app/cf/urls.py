from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from mixin.assets import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("applicants/", include("applicants.urls", namespace="applicants")),
    path("applications/", include("applications.urls", namespace="applications")),
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)