from . import views
from django.urls import path

urlpatterns = [
    path('', views.BookList.as_view(), name='home'),
    path('<int:book_id>/', views.update_book, name="update_book"),
    path('add-book/', views.AddBookView.as_view(), name="add_book"),
    path('/', views.create_book, name='create_book'),
]
