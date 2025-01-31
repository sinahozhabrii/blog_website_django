from django.db import models
from django.shortcuts import reverse
# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('pub','published'),
        ('drft','draft')
    )
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    date_time_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES ,max_length=4)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_deatail',args = [self.id])


