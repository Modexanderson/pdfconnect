from enviromentalsciences.views import EnviromentalSciencesView, UploadBookView, search_books
from django.urls import path, include

urlpatterns = [
    path('', EnviromentalSciencesView.as_view(), name='enviromentalsciences' ),
    path('upload/',  UploadBookView.as_view(), name='enviromental-upload'),
    path('search_books/',  search_books, name='enviromentalsciences-search-books'),
]

