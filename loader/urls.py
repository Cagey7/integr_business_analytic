from django.urls import path

from . import views

urlpatterns = [
    path("load-company-data/", views.LoadCompanyData.as_view()),
]