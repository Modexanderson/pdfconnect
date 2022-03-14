from django.contrib import admin
from django.urls import path, include
from home.views import HomeView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', book_list, name='home'),

    path('', include('home.urls')),
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

