from django.contrib import admin
from .models import Category, Post

# Register your models here.

class CateoryAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    
class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


admin.site.register(Category, CateoryAdmin)
admin.site.register(Post, PostAdmin)