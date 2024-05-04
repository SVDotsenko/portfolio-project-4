"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.views.generic import TemplateView
from django.views.defaults import (
    page_not_found as default_page_not_found,
    server_error as default_server_error,
    permission_denied as default_permission_denied,
)

urlpatterns = [
    path('', lambda request: redirect('account_login')),
    path("books/", include("book.urls")),
    path("authors/", include("author.urls")),
    path("profile/", include("reader.urls")),
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('403/', TemplateView.as_view(template_name="403.html"), name='403'),
]


def custom_permission_denied(request, exception):
    """
    Custom view for handling permission denied errors.

    Args:
        request (HttpRequest): The request object.
        exception (Exception): The exception that caused the permission denied
        error.

    Returns:
        HttpResponse: The response object with the updated template name.
    """
    response = default_permission_denied(request, exception)
    response.template_name = '403.html'
    return response


def custom_page_not_found(request, exception):
    """
    Custom handler for page not found (404) errors.

    Args:
        request (HttpRequest): The HTTP request object.
        exception (Exception): The exception that triggered the 404 error.

    Returns:
        HttpResponse: The response with the custom 404 page.
    """
    response = default_page_not_found(request, exception)
    response.template_name = '404.html'
    return response


def custom_server_error(request):
    """
    Custom view for handling server errors (500).

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object with the custom error template.
    """
    response = default_server_error(request)
    response.template_name = '500.html'
    return response
