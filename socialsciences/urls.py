from socialsciences.views import SocialSciencesView, UploadBookView, search_books
from django.urls import path, include

urlpatterns = [
    path('', SocialSciencesView.as_view(), name='socialsciences' ),
    path('upload/',  UploadBookView.as_view(), name='social-upload'),
    path('search_books/',  search_books, name='socialsciences-search-books'),


]

