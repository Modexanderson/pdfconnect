from pharmaceuticalsciences.views import PharmaceuticalSciencesView, UploadBookView, search_books
from django.urls import path, include

urlpatterns = [
    path('', PharmaceuticalSciencesView.as_view(), name='pharmaceuticalsciences' ),
    path('upload/',  UploadBookView.as_view(), name='pharmaceutical-upload'),
    path('search_books/',  search_books, name='pharmaceuticalsciences-search-books'),


]

