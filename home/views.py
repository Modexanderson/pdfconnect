from django.core.paginator import Paginator
from django.views import generic
# from . import models




class HomeView(generic.TemplateView):
    template_name = 'home/home_page.html'
    # model = models.Book
    paginate_by = 10


# class UploadBookView(generic.CreateView):
#     model = models.Book
#     form_class = BookForm
#     success_url = reverse_lazy('art')
#     template_name = 'home/upload_page.html'

