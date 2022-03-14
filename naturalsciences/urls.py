from naturalsciences.views import NaturalSciencesView, UploadBookView, search_books
from django.urls import path, include

urlpatterns = [
    path('', NaturalSciencesView.as_view(), name='naturalsciences' ),
    path('upload/',  UploadBookView.as_view(), name='natural-upload'),
    path('search_books/',  search_books, name='naturalsciences-search-books'),


]

