from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import path

from library.utils import is_admin
from . import views
from .views import BookDetail, BookList

urlpatterns = [
    path('', login_required(BookList.as_view()), name='books'),
    path('add/',
         user_passes_test(is_admin, login_url='403')(BookDetail.as_view()),
         name="add_book"),
    path('update/<int:book_id>/',
         user_passes_test(is_admin, login_url='403')(BookDetail.as_view()),
         name="update_book"),
    path('delete/<int:book_id>/',
         user_passes_test(is_admin, login_url='403')(BookList.as_view()),
         name="delete_book"),
    path('toggle_reader/<int:book_id>/', views.toggle_reader,
         name="toggle_reader"),
]
