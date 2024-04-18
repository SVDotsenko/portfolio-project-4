from django.contrib.auth.decorators import user_passes_test
from django.urls import path

from .views import AuthorList, AuthorDetail


def is_admin(user):
    return user.is_superuser


urlpatterns = [
    path('', user_passes_test(is_admin, login_url='403')(AuthorList.as_view()),
         name='authors'),
    path('author/', AuthorDetail.as_view(), name="add_author"),
    path('author/<int:author_id>/', AuthorDetail.as_view(),
         name="update_author"),
    path('author/<int:author_id>/delete', AuthorList.as_view(),
         name="delete_author"),
]
