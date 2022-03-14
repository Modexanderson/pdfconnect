from managementsciences.views import ManagementSciencesView, UploadBookView, search_books
from django.urls import path, include

urlpatterns = [
    path('', ManagementSciencesView.as_view(), name='managementsciences' ),
    path('upload/',  UploadBookView.as_view(), name='management-upload'),
    path('search_books/',  search_books, name='managementsciences-search-books'),


]

