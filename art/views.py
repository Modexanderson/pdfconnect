from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Q

from . import models
from .forms import BookForm


class ArtView(generic.ListView):
    template_name = 'home/art_page.html'
    model = models.Book
    paginate_by = 10    


class UploadBookView(generic.CreateView):
    model = models.Book
    form_class = BookForm
    success_url = reverse_lazy('art')
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


# def detail(request, object_id):
#     context = {}
#     context["data"] = models.Book.objects.get(id=object_id)
#     return render(request, 'home/detail.html', context)


# def delete_book(request, pk):
#     if request.method == 'POST':
#         book = models.Book.objects.get(pk=pk)
#         book.delete()
#     return redirect('book_list')

