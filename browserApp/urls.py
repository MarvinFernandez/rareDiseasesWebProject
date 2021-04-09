from django.urls import path

from. import views
#path('url_en_el_buscador', ruta_documento, name="nombre_a_usar")
urlpatterns = [
    path('', views.FinderView, name="Browser"), 
    path('disease/<int:disease_id>/', views.DiseasesView, name="DiseasesTemplate"),#<columna dentro de BDD>
    path('resource/<int:resource_id>/', views.ResourceView, name="ResourceTemplate"),
    path('resourcestypes/<int:resourcestype_id>/', views.ResourceTypeView, name="ResourcestypesTemplate"),

    path('diseaseBw/', views.DiseaseBrowserView, name="DiseaseBw"),
    path('resourceBw/', views.ResourceBrowserView, name="ResourceBw"),
    path('resourcestypeBw/', views.ResourcestypeBrowserView, name="ResourcestypeBw"),
    path('urlBw/', views.UrlBrowserView, name="UrlBw"),
   
    path('diseaseBw/results/', views.DiseaseResultsView, name="DiseaseResults"),
    path('resourceBw/results/', views.ResourceResultsView, name="ResourceResults"),
    path('resourcestypeBw/results/', views.ResourcestypeResultsView, name="ResourcestypeResults"),
    path('urlBw/results/', views.UrlResultsView, name="UrlResults"),
]