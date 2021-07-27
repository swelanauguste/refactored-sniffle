from django.contrib import admin
from django.urls import path, include

from mixin.assets import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("applicants/", include("applicants.urls", namespace="applicants")),
    path("admin/", admin.site.urls),
]
