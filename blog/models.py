from django.db import models
from django.conf import settings


# Create your models here.

#User = settings.AUTH_USER

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,verbose_name='url',unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category',kwargs={'slug':self.slug})


    class Meta:
        ordering = ['title']



class Tag(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,verbose_name='url',unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Post(models.Model):
    author = models.CharField(max_length=120)
    content = models.TextField(blank=True)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Опубликовано')
    slug = models.SlugField(max_length=255,verbose_name='url',unique=True)
    #photo = models.ImageField(upload_to='photos/',blank=True)
    views = models.IntegerField(default=0,verbose_name='кол-во просмотров')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='posts')
    tags = models.ManyToManyField(Tag,blank=True,null=True,related_name='posts')


    class Meta:
        ordering = ['-created_at']


    def get_absolute_url(self):
        return reverse('post:detail')
