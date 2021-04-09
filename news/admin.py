from django.contrib import admin
from .models import Category, Post

# Register your models here.

class CateoryAdmin(admin.ModelAdmin):
    list_filter=("updated",)
    readonly_fields=('created','updated')
    date_hierarchy=('updated')
    
class PostAdmin(admin.ModelAdmin):
    list_filter=("updated",)
    readonly_fields=('created','updated')
    date_hierarchy=('updated')


admin.site.register(Category, CateoryAdmin)
admin.site.register(Post, PostAdmin)