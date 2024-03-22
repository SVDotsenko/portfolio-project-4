from . import views
from django.urls import path

urlpatterns = [
    path('', views.BookList.as_view(), name='home'),
    path('<int:book_id>/', views.book_edit, name="book_edit"),
    path('add-book/', views.AddBookView.as_view(), name="add_book"),
]
