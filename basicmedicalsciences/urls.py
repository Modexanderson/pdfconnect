from basicmedicalsciences.views import BasicMedicalSciencesView, UploadBookView, search_books
from django.urls import path, include

urlpatterns = [
    path('', BasicMedicalSciencesView.as_view(), name='basicmedicalsciences' ),
    path('upload/',  UploadBookView.as_view(), name='basic-upload'),
    path('search_books/',  search_books, name='basicmedicalsciences-search-books'),

]

