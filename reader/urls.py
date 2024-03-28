from django.urls import path

from . import views

urlpatterns = [
    path('', views.ReaderDetail.as_view(), name='reader'),
]
