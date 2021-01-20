from django.db import models


class Blog(models.Model):

    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True, null=True)
    author = models.CharField(max_length=50)
    story = models.CharField(max_length=10000)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title