from . import views
from django.urls import path

urlpatterns = [
    path('', views.BookList.as_view(), name='home'),
    path('book/', views.BookDetail.as_view(), name="add_book"),
    path('book/<int:book_id>/', views.BookDetail.as_view(), name="update_book"),
    path('book/<int:book_id>/delete', views.BookList.as_view(),
         name="delete_book"),
]
