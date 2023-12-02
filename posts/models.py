from django.db import models
from django.utils import timezone

# Create your models here.
class Poster(models.Model):
    poster_header = models.CharField(max_length=155)
    poster_content = models.TextField()
    poster_date = models.DateField(default=timezone.datetime.now)
    poster_img = models.ImageField(null=True, blank=True, upload_to='media')

    def __str__(self):
        return f'The New Post name: {self.poster_header}!'

