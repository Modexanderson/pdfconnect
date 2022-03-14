from law.views import LawView, UploadBookView, search_books
from django.urls import path, include

urlpatterns = [
    path('', LawView.as_view(), name='law' ),
    path('upload/',  UploadBookView.as_view(), name='upload'),
    path('search_books/',  search_books, name='law-search-books'),


]

