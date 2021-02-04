from django.urls import path

from. import views
#path('url_en_el_buscador', ruta_documento, name="nombre_a_usar")
urlpatterns = [
    path('', views.News, name="News"),
    path('category/<int:category_id>/', views.CategoryView, name="Category")#<columna dentro de BDD>
]