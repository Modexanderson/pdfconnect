from engineering.views import EngineeringView, UploadBookView, search_books
from django.urls import path, include

urlpatterns = [
    path('', EngineeringView.as_view(), name='engineering' ),
    path('upload/',  UploadBookView.as_view(), name='engineering-upload'),
    path('search_books/',  search_books, name='engineering-search-books'),


]

