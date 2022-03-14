from agriculture.views import AgricultureView, UploadBookView, search_books
from django.urls import path

urlpatterns = [
    path('', AgricultureView.as_view(), name='agriculture' ),
    path('upload/',  UploadBookView.as_view(), name='agriculture-upload'),
    path('search_books/',  search_books, name='agriculture-search-books'),


]

