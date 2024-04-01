from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import BookDetail, BookList

urlpatterns = [
    path('', login_required(BookList.as_view()), name='home'),
    path('book/', BookDetail.as_view(), name="add_book"),
    path('book/<int:book_id>/', BookDetail.as_view(), name="update_book"),
    path('book/<int:book_id>/delete', BookList.as_view(), name="delete_book"),
]
