from django.contrib import admin
from .models import Diseases, Resourcestype, Url, Resources

class DiseasesAdmin (admin.ModelAdmin):
    list_filter=("affectedsystem",)
    list_display=["diseasename", "prevalence", "affectedsystem"]
    #readonly_fields=('created','updated')

class ResourcestypeAdmin (admin.ModelAdmin):
    list_display=['Type']
    #list_filter=("finality",)
    #readonly_fields=('created','updated')
    
class UrlAdmin (admin.ModelAdmin):
    list_filter=("language", "location")
    list_display=['language','location','address']
    #readonly_fields=('created','updated')

class ResourcesAdmin (admin.ModelAdmin):
    list_filter=("finality", "price", "access")
    list_display=['name', 'finality', 'price', 'access']
    #readonly_fields=('created','updated')
 
admin.site.register(Diseases, DiseasesAdmin)
admin.site.register(Resourcestype, ResourcestypeAdmin)
admin.site.register(Url, UrlAdmin)
admin.site.register(Resources, ResourcesAdmin) 
"""
admin.site.register(Diseases)
admin.site.register(Resourcestype)
admin.site.register(Url)
admin.site.register(Resources) """