from django.urls import path

from .views import AuthorList, AuthorDetail

urlpatterns = [
    path('', AuthorList.as_view(), name='authors'),
    path('add/', AuthorDetail.as_view(), name="add_author"),
    path('update/<int:author_id>/', AuthorDetail.as_view(),
         name="update_author"),
    path('delete/<int:author_id>/', AuthorList.as_view(),
         name="delete_author"),
]
