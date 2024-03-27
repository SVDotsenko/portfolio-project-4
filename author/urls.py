from . import views
from django.urls import path

urlpatterns = [
    path('', views.AuthorList.as_view(), name='authors'),
    path('author/', views.AuthorDetail.as_view(), name="add_author"),
    path('author/<int:author_id>/', views.AuthorDetail.as_view(),
         name="update_author"),
    path('author/<int:author_id>/delete', views.AuthorList.as_view(),
         name="delete_author"),
]
