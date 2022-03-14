from home.views import HomeView
from django.urls import path, include

urlpatterns = [
    path('', HomeView.as_view(), name='home' ),
    # path('upload/',  UploadBookView.as_view(), name='upload'),

]

