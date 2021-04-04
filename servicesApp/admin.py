from django.contrib import admin
from .models import Diseases, Resourcestype, Url, Resources

""" class DiseasesAdmin (admin.ModelAdmin):

    readonly_fields=('created','updated')

class ResourcestypeAdmin (admin.ModelAdmin):

    readonly_fields=('created','updated')
    
class UrlAdmin (admin.ModelAdmin):

    readonly_fields=('created','updated')

class ResourcesAdmin (admin.ModelAdmin):

    readonly_fields=('created','updated')

admin.site.register(Diseases, DiseasesAdmin)
admin.site.register(Resourcestype, ResourcestypeAdmin)
admin.site.register(Url, UrlAdmin)
admin.site.register(Resources, ResourcesAdmin) """