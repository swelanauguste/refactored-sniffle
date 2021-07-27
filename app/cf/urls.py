from django.contrib import admin
from django.urls import path, include

from mixin.assets import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("applicants/", include("applicants.urls", namespace="applicants")),
    path("applications/", include("applications.urls", namespace="applications")),
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
]
