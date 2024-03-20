from . import views
from django.urls import path

urlpatterns = [
    path('', views.BookList.as_view(), name='home'),
    path('<int:id>/', views.book_edit, name="book_edit"),
]
