from dentalsciences.views import DentalSciencesView, UploadBookView, search_books
from django.urls import path, include

urlpatterns = [
    path('', DentalSciencesView.as_view(), name='dentalsciences' ),
    path('upload/',  UploadBookView.as_view(), name='dental-upload'),
    path('search_books/',  search_books, name='dentalsciences-search-books'),

]

