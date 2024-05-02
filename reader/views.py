from django.contrib import messages
from django.contrib.auth import get_user
from django.http import HttpResponseServerError
from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
from book.models import Book
from reader.forms import ProfileImageForm
from reader.models import ProfileImage


class ProfileDetail(View):
    def get(self, request):
        """
        Handles the GET request for the reader view.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: The HTTP response object containing the rendered template.
        """
        reader = get_user(request)
        books = Book.objects.filter(reader=reader)
        image = ProfileImage.objects.filter(user=reader)
        if image:
            reader.image = image[0].image
        context = {'reader': reader, 'books': books, 'DEBUG': settings.DEBUG}
        return render(request, "reader/reader.html", context)

    def post(self, request):
        """
        Handle the POST request for updating user profile.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponseRedirect: Redirects to the 'books' page.

        Raises:
            HttpResponseServerError: If 'emulate-error' parameter is present in the request.
        """
        if request.POST.get('emulate-error'):
            raise HttpResponseServerError()
        if request.FILES.get('fileInput'):
            self.save_image(request)
        user = get_user(request)
        user.first_name = request.POST['first-name']
        user.last_name = request.POST['last-name']
        user.email = request.POST['email']
        user.save()
        messages.add_message(request, messages.SUCCESS,
                             f'Updated profile for {user}')
        return redirect('books')

    def save_image(self, request):
        """
        Saves the profile image for the user.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            None
        """
        reader = get_user(request)
        image = ProfileImage.objects.filter(user=reader).first()

        if image:
            image_form = ProfileImageForm(data=request.POST, instance=image)
        else:
            image_form = ProfileImageForm(data=request.POST)

        if image_form.is_valid():
            image = image_form.save(commit=False)
            image.image = request.FILES['fileInput']
            if not hasattr(image, 'user'):
                image.user = reader
            image.save()
