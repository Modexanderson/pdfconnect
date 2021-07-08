"""pdfs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home.views import HomeView, book_list
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', book_list, name='home'),

    path('home/', include('home.urls')),
    path('agriculture/', include('agriculture.urls')),
    path('art/', include('art.urls')),
    path('basicmedicalsciences/', include('basicmedicalsciences.urls')),
    path('clinicalsciences/', include('clinicalsciences.urls')),
    path('dentalsciences/', include('dentalsciences.urls')),
    path('education/', include('education.urls')),
    path('engineering/', include('engineering.urls')),
    path('enviromentalsciences/', include('enviromentalsciences.urls')),
    path('healthsciencesandtechnology/', include('healthsciencesandtechnology.urls')),
    path('law/', include('law.urls')),
    path('managementsciences/', include('managementsciences.urls')),
    path('naturalsciences/', include('naturalsciences.urls')),
    path('pharmaceuticalsciences/', include('pharmaceuticalsciences.urls')),
    path('socialsciences/', include('socialsciences.urls')),
    path('veterinarymedecine/', include('veterinarymedecine.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
 document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

