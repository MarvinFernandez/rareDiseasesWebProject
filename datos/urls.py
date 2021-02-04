from django.urls import path

from. import views
#path('url_en_el_buscador', ruta_documento, name="nombre_a_usar")
urlpatterns = [
    path('', views.Contacto, name="Contacto"),
]