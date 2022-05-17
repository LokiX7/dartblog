from django.db import models
from django.urls import reverse_lazy

class Category(models.Model):
    title = models.CharField('title', max_length=50)
    slug = models.SlugField('url', unique=True)

    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField('title', max_length=15)
    slug = models.SlugField('url', unique=True)

    def get_absolute_url(self):
        return reverse_lazy('tag', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        ordering = ['title']


class Post(models.Model):
    title = models.CharField('title', max_length=60)
    slug = models.SlugField('slug')
    author = models.CharField('author', max_length=100)
    content = models.TextField('content', max_length=255, blank=True)
    created_at = models.DateTimeField('created at', auto_now_add=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    views = models.IntegerField('views', default=0)
    rating = models.IntegerField('rating', default=0)
    is_published = models.BooleanField('is published', default=False)

    category = models.ForeignKey(
        Category, 
        on_delete=models.PROTECT,
        related_name='posts'
    )
    tags = models.ManyToManyField(
        Tag, 
        blank=True,
        related_name='posts'
    )

    def get_absolute_url(self):
        return reverse_lazy('post', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ['-created_at', '-views']

