from veterinarymedecine.views import VeterinaryMedicineView, UploadBookView, search_books
from django.urls import path

urlpatterns = [
    path('', VeterinaryMedicineView.as_view(), name='veterinarymedicine' ),
    path('upload/',  UploadBookView.as_view(), name='veterinary-upload'),
    path('search_books/',  search_books, name='veterinarymedicine-search-books'),
]

