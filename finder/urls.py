from django.urls import path

from. import views
#path('url_en_el_buscador', ruta_documento, name="nombre_a_usar")
urlpatterns = [
    path('', views.FinderView, name="Browser"),
    path('results/', views.Results, name="Results"),
    path('disease/<int:disease_id>/', views.DiseasesView, name="DiseasesTemplate"),#<columna dentro de BDD>
    path('resource/<int:resource_id>/', views.ResourceView, name="ResourceTemplate"),
    path('resourcestypes/<int:resourcestype_id>/', views.ResourceTypeView, name="ResourcestypesTemplate"),
]