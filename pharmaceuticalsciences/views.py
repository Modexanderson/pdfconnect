import imp
from django.core.paginator import Paginator
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render
from django.db.models import Q

from . import models
from .forms import BookForm



class PharmaceuticalSciencesView(generic.ListView):
    template_name = 'home/pharmaceuticalsciences_page.html'
    model = models.Book
    paginate_by = 10


class UploadBookView(generic.CreateView):
    model = models.Book
    form_class = BookForm
    success_url = reverse_lazy('pharmaceuticalsciences')
    template_name = 'home/upload_page.html'


def search_books(request):
    if request.method == "POST":
        search = request.POST['search']
        books = models.Book.objects.filter(Q(title__contains=search) | Q(author__contains=search))
        return render(request, 'home/search_books.html', {
            'search' : search, 'books' : books
        })
    else:
        return render(request, 'home/search_books.html', {})
