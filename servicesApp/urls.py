from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

#Urls de la app
urlpatterns = [
    path('', views.Services, name="Services"),
    path('diseases_Table/', views.DiseasesTable, name="DiseasesTable"),
    path('resources_Table/', views.ResourcesTable, name="ResourcesTable"),
    path('urls_Table/', views.UrlsTable, name="urlsTable"),
    path('resourcestype_Table/', views.ResourcestypeTable, name="resourcestypeTable"),
    path('resources_Table/<finality_id>/', views.ResourcesSelet, name="ResourcesSelet"),
]

#urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)