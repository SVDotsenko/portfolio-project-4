from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import ProfileDetail

urlpatterns = [
    path('', login_required(ProfileDetail.as_view()), name='profile'),
]
