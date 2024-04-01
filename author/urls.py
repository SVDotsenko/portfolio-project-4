from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import AuthorList, AuthorDetail

urlpatterns = [
    path('', login_required(AuthorList.as_view()), name='authors'),
    path('author/', AuthorDetail.as_view(), name="add_author"),
    path('author/<int:author_id>/', AuthorDetail.as_view(),
         name="update_author"),
    path('author/<int:author_id>/delete', AuthorList.as_view(),
         name="delete_author"),
]
