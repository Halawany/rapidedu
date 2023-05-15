from django.db import models
from django.urls import reverse

class Post(models.Model):

    title = models.CharField(max_length=650)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()
    slug = models.SlugField(unique=True, blank=False)
    cover = models.ImageField(upload_to='images/blog/covers')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])