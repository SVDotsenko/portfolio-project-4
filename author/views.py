from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from author.models import Author


class AuthorList(View):
    def get(self, request, author_id=-1):
        authors = Author.objects.all()
        if author_id < 0:
            context = {'object_list': authors}
            return render(request, "author/index.html", context)
        get_object_or_404(authors, id=author_id).delete()
        return redirect('authors')


class AuthorDetail(View):
    pass