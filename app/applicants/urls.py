from django.urls import path

from . import views

app_name = 'applicants'


urlpatterns = [
    path('create', views.ApplicantCreateView.as_view(), name='applicant-create'),
    path('detail/<int:pk>', views.ApplicantDetailView.as_view(), name='applicant-detail'),
]