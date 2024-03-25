from . import views
from django.urls import path

urlpatterns = [
    path('', views.BookList.as_view(), name='home'),
    path('add-book/', views.AddBookView.as_view(), name="add_book"),
    path('/', views.create_update_book, name='create_book'),
    path('<int:book_id>/', views.create_update_book, name="update_book"),
    path('<int:book_id>/delete', views.delete_book, name="delete_book"),
]
