from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='category' 
        verbose_name_plural='categories'

    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=50)
    image=models.ImageField(upload_to="news", null=True, blank=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)# relacion 1-Manycuando se elimina un usuario borra en cascada todos sus post
    categories=models.ManyToManyField(Category)#relacion Many-Many (Post-Category)
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'

    def __str__(self):
        return self.title