from django.contrib.auth import get_user
from django.shortcuts import render
from django.views import View


class ReaderDetail(View):
    def get(self, request):
        context = {'reader': get_user(request)}
        return render(request, "reader/reader.html", context)
