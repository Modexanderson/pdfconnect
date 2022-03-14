from healthsciencesandtechnology.views import HealthSciencesAndTechnologyView, UploadBookView, search_books
from django.urls import path, include

urlpatterns = [
    path('', HealthSciencesAndTechnologyView.as_view(), name='healthsciencesandtechnology' ),
    path('upload/',  UploadBookView.as_view(), name='health-upload'),
    path('search_books/',  search_books, name='healthsciencesandtecnology-search-books'),


]

