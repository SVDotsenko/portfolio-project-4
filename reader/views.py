from django.contrib.auth import get_user
from django.shortcuts import render, redirect
from django.views import View


class ReaderDetail(View):
    def get(self, request):
        context = {'reader': get_user(request)}
        return render(request, "reader/reader.html", context)

    def post(self, request):
        user = get_user(request)
        user.username = request.POST['username']
        user.first_name = request.POST['first-name']
        user.last_name = request.POST['last-name']
        user.email = request.POST['email']
        user.save()
        return redirect('home')
