from .views import ArtView, UploadBookView, search_books
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', ArtView.as_view(), name='art' ),
    path('upload/',  UploadBookView.as_view(), name='art-upload'),
    path('search_books/',  search_books, name='art-search-books'),
    # path('object/', detail, name='detail'),
    
] 
