from django.urls import path

from rareDiseasesWebApp import views
from django.conf import settings
from django.conf.urls.static import static

#Urls de la app path('url_en_el_buscador', ruta_documento, name="nombre_a_usar")
urlpatterns = [
    path('', views.home, name="Home"),
]

#añade la url como media
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 