from django.contrib.auth import get_user
from django.http import HttpResponseServerError
from django.shortcuts import render, redirect
from django.views import View
from book.models import Book
from reader.forms import AddProfileImageForm
from reader.models import ProfileImage


class ReaderDetail(View):
    def get(self, request):
        reader = get_user(request)
        books = Book.objects.filter(reader=reader)
        image = ProfileImage.objects.filter(user=reader)
        if image:
            reader.image = image[0].image
        context = {'reader': reader, 'books': books}
        return render(request, "reader/reader.html", context)

    def post(self, request):
        if request.POST.get('emulate-error'):
            raise HttpResponseServerError()
        if request.FILES.get('fileInput'):
            self.save_image(request)
        user = get_user(request)
        user.first_name = request.POST['first-name']
        user.last_name = request.POST['last-name']
        user.email = request.POST['email']
        user.save()
        return redirect('books')

    def save_image(self, request):
        reader = get_user(request)
        image = ProfileImage.objects.filter(user=reader).first()

        if image:
            image_form = AddProfileImageForm(data=request.POST, instance=image)
        else:
            image_form = AddProfileImageForm(data=request.POST)

        if image_form.is_valid():
            image = image_form.save(commit=False)
            image.image = request.FILES['fileInput']
            if not hasattr(image, 'user'):
                image.user = reader
            image.save()
