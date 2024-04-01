from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import ReaderDetail

urlpatterns = [
    path('', login_required(ReaderDetail.as_view()), name='reader'),
]
