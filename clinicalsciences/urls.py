from clinicalsciences.views import ClinicalSciencesView, UploadBookView, search_books
from django.urls import path, include

urlpatterns = [
    path('', ClinicalSciencesView.as_view(), name='clinicalsciences' ),
    path('upload/',  UploadBookView.as_view(), name='clinical-upload'),
    path('search_books/',  search_books, name='clinicalsciences-search-books'),


]

