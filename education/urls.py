from education.views import EducationView, UploadBookView, search_books
from django.urls import path, include

urlpatterns = [
    path('', EducationView.as_view(), name='education' ),
    path('upload/',  UploadBookView.as_view(), name='education-upload'),
    path('search_books/',  search_books, name='education-search-books'),

]

