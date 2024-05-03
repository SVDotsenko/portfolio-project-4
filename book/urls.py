from django.urls import path

from . import views
from .views import BookDetail, BookList

urlpatterns = [
    path('', BookList.as_view(), name='books'),
    path('add/', BookDetail.as_view(), name="add_book"),
    path('update/<int:book_id>/', BookDetail.as_view(), name="update_book"),
    path('delete/<int:book_id>/', BookList.as_view(), name="delete_book"),
    path('toggle_reader/<int:book_id>/', views.toggle_reader,
         name="toggle_reader"),
]
